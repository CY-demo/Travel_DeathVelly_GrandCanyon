# Canyon Field Guide · 峽谷隨行

A mobile-friendly Traditional Chinese travel guide to Death Valley, the Grand Canyon South Rim, Upper Antelope Canyon, Horseshoe Bend, and Las Vegas airport lounges.

**[Open the current live demo](https://canyon-field-guide.workspace-721786.chatgpt.site)**

## Built with AI

This website was built with substantial AI assistance using ChatGPT and Codex. AI helped generate the application code, page layouts, and initial travel explanations. I defined the travel requirements, supplied itinerary details and tour-operator correspondence, and refined the experience through iterative feedback. The project explores how AI-assisted development can turn a practical family travel need into a usable, mobile-friendly offline guide.

## What it does

- Organizes 31 reading chapters into three sightseeing days and an airport guide.
- Explains landscape formation alongside practical sightseeing notes and source links.
- Supports larger text, expandable chapters, and direct chapter navigation.
- Saves text, photographs, and application files for offline reading on each device.
- Remembers reading preferences locally, without a sign-in or backend.

## Technology

Plain HTML, CSS, and JavaScript; JSON content; a web app manifest; and a service worker using the Cache API. No framework, build step, or API key is required. There is no runtime AI service or audio narration.

## Run locally

From this repository, run:

```sh
python3 -m http.server 8000 --directory dist
```

Then open `http://localhost:8000`. Service workers require HTTPS or localhost. Run `node verify.mjs` for the static asset and offline-cache checks.

## GitHub Pages

Repository: [CY-demo/Travel_DeathVelly_GrandCanyon](https://github.com/CY-demo/Travel_DeathVelly_GrandCanyon). After Pages is enabled and deployment succeeds, the website address will be `https://cy-demo.github.io/Travel_DeathVelly_GrandCanyon/`.

In the repository settings, select **Pages → Source → GitHub Actions**. The included workflow publishes `dist/` whenever changes are pushed to `main`, or when run manually. Its successful deployment displays the public Pages URL. The manifest and asset paths support a project subdirectory.

## Offline use

Open the website while connected, choose **離線與使用**, and download the offline content. Repeat on every device and download again after content updates. Test with airplane mode before traveling. External source links still require connectivity, and browsers may remove stored content. Offline downloads on the original demo do not transfer to a different hosting domain.

## Content and image credits

Official park, tour-operator, and lounge references are linked in the guide and in `dist/content.json`. Photographs are credited in the website footer: Death Valley and Horseshoe Bend images from the U.S. National Park Service; Grand Canyon image credited to NPS / T. Karlovetz. Third-party names, photographs, and source materials retain their respective terms; this repository does not grant additional rights to them.

Travel details are a dated planning reference, not a guarantee of access, schedules, prices, or tour stops. The public version excludes private booking records and traveler contact details.
