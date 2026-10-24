## architek.earth

architek.earth — an independent data studio. Pay-per-result scrapers with recorded runs, published canaries and stable schemas, built for people and AI agents.

**Code like concrete.**

All actors run on [Apify](https://apify.com/architekture). Copy-paste code for every one of them, in Python, Node, curl and n8n, is in [**examples**](https://github.com/architek-earth/examples).

### The promise

- **You pay for delivered results, nothing else.** A blocked page, an invalid input or an empty search returns a free status row that says what happened.
- **Runs finish cleanly.** If a run is stopped or hits its timeout, you keep what was collected. You are never charged twice for the same row.
- **Recorded runs.** Listings quote real runs: rows delivered, inputs and duration.
- **Published canaries.** Scheduled test runs check the actors against the live sites, so breakage is caught early.
- **Stable schemas.** Output fields are add-only. We never rename or remove a field you depend on.

### For AI agents

Every live actor is a ready-to-paste MCP server entry in [**mcp**](https://github.com/architek-earth/mcp): the Apify MCP server at `mcp.apify.com`, scoped to one actor, with your token read from `APIFY_TOKEN`. Regenerated weekly from the catalog below.

## Catalog

<!-- catalog:start -->
**27 live actors.** Prices are per delivered result; status rows are free.

### Grocery and retail prices

| Actor | What you get | Price |
|---|---|---|
| [Woolworths AU Scraper](https://apify.com/architekture/woolworths-au-product-scraper) | Woolworths Australia (woolworths.com.au) scraper: product name, brand, size, price, was price, savings, specials, unit price, barcode,… | $1.50 / 1,000 · Product |
| [Coles Scraper](https://apify.com/architekture/coles-au-product-scraper) | Coles Australia (coles.com.au) scraper: product name, brand, size, price, was price, savings, specials, multi-buy, unit price, category,… | $1.50 / 1,000 · Product |
| [ALDI AU Scraper](https://apify.com/architekture/aldi-au-product-scraper) | ALDI Australia (aldi.com.au) scraper: product name, brand, pack size, price, was price, savings, specials, unit price, Special Buys… | $1.50 / 1,000 · Product |
| [Woolworths NZ Scraper](https://apify.com/architekture/woolworths-nz-scraper) | Woolworths New Zealand (woolworths.co.nz, ex-Countdown) product data: prices, was prices, specials, club prices, multi-buys, promotion… | $1.00 / 1,000 · Product |
| [New World NZ Scraper](https://apify.com/architekture/new-world-nz-scraper) | New World NZ (newworld.co.nz) scraper: store, product ID, name, brand, size, shelf price, Clubcard price, unit price, promotions,… | $4.00 / 1,000 · Product + $0.15 per collection delivered |
| [Pak'nSave Scraper](https://apify.com/architekture/paknsave-nz-scraper) | Pak'nSave New Zealand (paknsave.co.nz) scraper: product ID, name, brand, package size, price in NZD, unit price, unit label, promotions,… | $4.00 / 1,000 · Product + $0.15 per collection delivered |
| [Tesco UK Scraper](https://apify.com/architekture/tesco-uk-scraper) | Tesco UK (tesco.com) scraper: product ID, TPNB, TPNC, GTIN barcode, title, brand, price, unit price, Clubcard price, promotions, offer… | $2.00 / 1,000 · Product |
| [Sainsbury's Scraper](https://apify.com/architekture/sainsburys-uk-scraper) | Sainsbury's UK (sainsburys.co.uk) scraper: product name, price, unit price, offers, promotions, EAN barcodes, labels, reviews, rating,… | $2.00 / 1,000 · Product |
| [ALDI Ireland Scraper](https://apify.com/architekture/aldi-ie-scraper) | ALDI Ireland (aldi.ie) scraper: product name, brand, size, price in EUR, was price, saving, unit price, availability, Specialbuys… | $1.00 / 1,000 · Product |
| [Dunnes Stores Scraper](https://apify.com/architekture/dunnes-ie-scraper) | Dunnes Stores Ireland (dunnesstores.com) fashion and home scraper: name, brand, EUR price, sale price, sizes, colours, SKU, EAN barcode,… | $1.00 / 1,000 · Product |
| [Mercadona Scraper](https://apify.com/architekture/mercadona-es-scraper) | Mercadona Spain (tienda.mercadona.es) scraper: name, brand, packaging, size, EUR price, unit price, previous price, VAT rate, category… | $1.00 / 1,000 · Product |

### E-commerce and marketplaces

| Actor | What you get | Price |
|---|---|---|
| [Shopify Scraper](https://apify.com/architekture/shopify-products-scraper) | Shopify store scraper for any public Shopify storefront, worldwide: products, variant prices, compare-at (sale) prices, SKUs,… | $0.50 / 1,000 · Product |
| [TikTok Shop Scraper](https://apify.com/architekture/tiktok-shop-products-scraper) | TikTok Shop US (shop.tiktok.com) products by keyword search: price, currency, seller ID and name, rating, review count, sold count and… | $3.00 / 1,000 · Product |
| [AliExpress Scraper](https://apify.com/architekture/aliexpress-search-scraper) | AliExpress global product search from aliexpress.com by keyword: sale price, original price, discount, currency, order count, rating,… | $2.50 / 1,000 · Product |

### Jobs, companies and people

| Actor | What you get | Price |
|---|---|---|
| [Indeed Scraper](https://apify.com/architekture/indeed-scraper) | Indeed US jobs from indeed.com: job title, company, location, full description, salary range and period, job type, remote or hybrid… | $3.50 / 1,000 · Job |
| [LinkedIn Jobs Scraper](https://apify.com/architekture/linkedin-jobs-monitor) | LinkedIn jobs (linkedin.com) public job search: title, company, location, posted date, description, salary with evidence, seniority,… | $4.00 / 1,000 · Delivered job |
| [Y Combinator Scraper](https://apify.com/architekture/yc-companies-scraper) | Y Combinator startup directory data from ycombinator.com: company name, batch, status, stage, industry, region, tags, team size,… | $2.00 / 1,000 · Company |

### Video, social and newsletters

| Actor | What you get | Price |
|---|---|---|
| [YouTube Transcript Scraper](https://apify.com/architekture/youtube-transcript-scraper) | YouTube transcripts, worldwide, from youtube.com: transcript text, timestamped segments, caption language, auto-generated flag,… | $4.00 / 1,000 · Transcript |
| [Unified Video Transcript API](https://apify.com/architekture/unified-transcript-api) | YouTube and TikTok video transcripts from youtube.com and tiktok.com in one JSON schema: transcript text, language, title, author,… | $1.00 / 1,000 · Transcript |
| [Threads Replies Scraper](https://apify.com/architekture/threads-replies-scraper) | Threads replies scraper, global, threads.com: reply and comment rows with author handle, name and verified badge, text, like, reply,… | $2.50 / 1,000 · Reply |
| [Substack Scraper](https://apify.com/architekture/substack-scraper) | Substack newsletter scraper (substack.com and custom domains): posts, authors, likes, comment counts, restacks, word counts, tags,… | $1.00 / 1,000 · Post |
| [Ad Intelligence Watchlist](https://apify.com/architekture/ad-intelligence-watchlist) | Meta Ad Library, any country (facebook.com/ads/library): new and changed Facebook and Instagram ads per advertiser since the last run:… | $1.50 / 1,000 · New or changed ad |

### Search, travel and trends

| Actor | What you get | Price |
|---|---|---|
| [Google Trends Scraper](https://apify.com/architekture/google-trends-scraper) | Google Trends Trending Now searches by country (title, approximate traffic, start time, related queries) and Explore keyword reports:… | $1.00 / 1,000 · Delivered Trending Now row |
| [Google Hotels Scraper](https://apify.com/architekture/google-hotels-scraper) | Google Hotels (google.com/travel/hotels) scraper: nightly prices, stay totals, currency, guest ratings, review counts, star class,… | $4.00 / 1,000 · Hotel property |
| [Google Shopping Scraper](https://apify.com/architekture/google-shopping-scraper) | Google Shopping scraper by keyword and country: title, price, sale price, merchant, rating, shipping and image per product; offers mode… | $3.00 / 1,000 · Delivered product |

### Sports

| Actor | What you get | Price |
|---|---|---|
| [Tennis Scraper](https://apify.com/architekture/tennis-data-scraper) | Flashscore tennis (global, flashscore.com): matches, live and final scores, set and tiebreak scores, point-by-point, match statistics,… | $2.50 / 1,000 · Delivered match or ranking |

### Documents

| Actor | What you get | Price |
|---|---|---|
| [EU E-Invoice Parser](https://apify.com/architekture/docparser-invoice-json) | EU e-invoices (XRechnung, ZUGFeRD, Factur-X, PEPPOL UBL) to JSON: invoice number, dates, seller and buyer VAT IDs, IBAN, net, tax and… | $2.00 / 1,000 · E-invoice |
<!-- catalog:end -->

<sub>Generated weekly from the public Apify Store listings.</sub>

## Recent updates

<!-- releases:start -->
2026-10-24 · [Google Hotels Scraper](https://apify.com/architekture/google-hotels-scraper) · 0.1.15 · README now answers blocked runs, stay dates, per-day calendars, filters and booking links up front; hero line from the 2026-10-24 canary run.

2026-10-24 · [Google Trends Scraper](https://apify.com/architekture/google-trends-scraper) · 0.1.26 · README answers the questions Google Trends users ask most: what happens on a block or page change, what a failed run costs, run times, keyword comparison, region coverage and integrations; the listing title now leads with interest over time, related queries and trending searches.

2026-10-24 · [Dunnes Stores Scraper](https://apify.com/architekture/dunnes-ie-scraper) · 0.0.212 · A search, category or product stopped as `BLOCKED` now saves the site's last response (redacted) in the run's key-value store so the cause can be checked; pricing, input and output are unchanged.

2026-10-24 · [ALDI Ireland Scraper](https://apify.com/architekture/aldi-ie-scraper) · 0.0.215 · A search, category or SKU stopped as `BLOCKED` now saves the site's last response (redacted) in the run's key-value store so the cause can be checked; pricing, input and output are unchanged.

2026-10-24 · [New World NZ Scraper](https://apify.com/architekture/new-world-nz-scraper) · 1.0.17 · A run stopped as `BLOCKED` now saves the site's last response (redacted) in the run's key-value store so the cause can be checked; pricing, input and output are unchanged.

2026-10-24 · [Woolworths NZ Scraper](https://apify.com/architekture/woolworths-nz-scraper) · 0.0.244 · A search or department refused as `BLOCKED` now saves the site's last response (redacted) in the run's key-value store so the cause can be checked; pricing, input and output are unchanged.

2026-10-24 · [Google Trends Scraper](https://apify.com/architekture/google-trends-scraper) · 0.1.25 · Keyword mode: the listing now shows the keyword price as $20.00 / 1,000 keyword reports ($0.02 each) instead of a per-row figure, and explains that rows delivered on a watch rerun are Google Trends churn; price and output unchanged.

2026-10-24 · [Pak'nSave Scraper](https://apify.com/architekture/paknsave-nz-scraper) · 0.0.32 · A run stopped as `BLOCKED` now saves the site's last response (redacted) in the run's key-value store, so the cause can be checked; pricing, input and output are unchanged.

2026-10-24 · [Tesco UK Scraper](https://apify.com/architekture/tesco-uk-scraper) · 1.0.22 · A failed proxy connection is now retried on a fresh proxy session before the run stops; pricing, input and output are unchanged.

2026-10-24 · [Google Trends Scraper](https://apify.com/architekture/google-trends-scraper) · 0.1.24 · Keyword mode: interest over time, interest by region and related queries for up to 20 keywords (`mode: "keyword"`), at $0.02 per keyword report.
<!-- releases:end -->

## Contact

- Email: [north@architek.earth](mailto:north@architek.earth)
- Something broken or missing? [Open an issue](https://github.com/architek-earth/.github/issues/new) or start a [discussion](https://github.com/architek-earth/.github/discussions).
