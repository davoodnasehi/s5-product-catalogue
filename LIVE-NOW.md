# Live mirror (while GitHub Pages provisions)

The catalogue is committed and public in this repo. GitHub Pages is enabled and both the
build and the deployment report **success**, but the Pages CDN is currently answering
`404 Site not found` for this account (reproduced on a second unrelated repo, so it is
account-level, not a mistake in this repo).

Until that resolves, the same files are served correctly here:

| What | URL |
|---|---|
| Catalogue index | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/index.html |
| RotaMon | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/products/rotamon.html |
| WearMon | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/products/wearmon.html |
| GETsmart | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/products/getsmart.html |
| Genset & lighting telematics | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/products/genset-lighting-telematics.html |
| Workshop line | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/products/workshop-line.html |
| Bus safety mesh | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/products/bus-safety-mesh.html |
| Bolt-tension (held) | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/products/bolt-tension-monitor.html |
| Manifest | https://raw.githack.com/davoodnasehi/s5-product-catalogue/main/manifest.json |

Browsable repo: https://github.com/davoodnassehi/s5-product-catalogue

**Preferred fix:** publish the same folder to the existing WordPress hosts
(mining-iot.com or s5system.com) under `/products/` — that also puts the pages on the
domains that already carry S5's search authority. Once the Pages CDN resolves, the
`https://davoodnassehi.github.io/s5-product-catalogue/` URLs in `manifest.json` and the
`canonical`/`og` tags become the live ones.

`raw.githack.com` is a development mirror (soft rate limit), not a permanent host.
