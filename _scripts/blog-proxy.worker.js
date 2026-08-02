// Cloudflare Worker: serves this blog at mmoustafa.com/blog/* and 301s the old host.
//
// Routes (both point at this one script):
//   mmoustafa.com/blog*   zone mmoustafa.com  -> proxy GitHub Pages
//   blog.0xmmo.co/*       zone 0xmmo.co       -> 301 to the new home
//
// Requires, in the same change: _config.yml url=https://mmoustafa.com + baseurl=/blog,
// and deleting the CNAME file so Pages serves 0xmmo.github.io directly instead of
// 301ing to blog.0xmmo.co (which would loop).
//
// Rollback: delete both routes. Restore CNAME + _config.yml to revert fully.

const ORIGIN = "https://0xmmo.github.io";
const PREFIX = "/blog";

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // Old home: 301 every path to the new subfolder, preserving query.
    if (url.hostname === "blog.0xmmo.co") {
      return Response.redirect(
        "https://mmoustafa.com" + PREFIX + url.pathname + url.search,
        301
      );
    }

    // New home: strip /blog and proxy GitHub Pages.
    // This also covers the project sites (/blog/forensics/, /blog/mmmail/),
    // which live in separate repos but serve under the same Pages host.
    let path = url.pathname.startsWith(PREFIX)
      ? url.pathname.slice(PREFIX.length)
      : url.pathname;
    if (path === "") {
      return Response.redirect(url.origin + PREFIX + "/" + url.search, 301);
    }

    const upstream = new Request(ORIGIN + path + url.search, request);
    const res = await fetch(upstream, { redirect: "manual" });

    // Pages redirects to absolute github.io URLs (e.g. a directory without a
    // trailing slash). Rewrite those so users stay under /blog.
    const loc = res.headers.get("location");
    if (loc) {
      const l = new URL(loc, ORIGIN);
      if (l.hostname === "0xmmo.github.io") {
        const out = new Response(res.body, res);
        out.headers.set("location", PREFIX + l.pathname + l.search);
        return out;
      }
    }
    return res;
  },
};
