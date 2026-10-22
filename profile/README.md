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

## Catalog

<!-- catalog:start -->
**26 live actors.** Prices are per delivered result; status rows are free.

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
| [TikTok Shop Scraper](https://apify.com/architekture/tiktok-shop-products-scraper) | Collect public US TikTok Shop products, prices, sellers, ratings and variants. | $3.00 / 1,000 · Product |
| [AliExpress Scraper](https://apify.com/architekture/aliexpress-search-scraper) | AliExpress global product search from aliexpress.com by keyword: sale price, original price, discount, currency, order count, rating,… | $2.50 / 1,000 · Product |

### Jobs, companies and people

| Actor | What you get | Price |
|---|---|---|
| [Indeed Scraper](https://apify.com/architekture/indeed-scraper) | Search US Indeed jobs by keyword and location. | $3.50 / 1,000 · Job |
| [LinkedIn Jobs Scraper](https://apify.com/architekture/linkedin-jobs-monitor) | Public LinkedIn jobs with descriptions, salary evidence and saved continuation. | $4.00 / 1,000 · Delivered job |
| [Y Combinator Scraper](https://apify.com/architekture/yc-companies-scraper) | Y Combinator startup directory data from ycombinator.com: company name, batch, status, stage, industry, region, tags, team size,… | $2.00 / 1,000 · Company |

### Video, social and newsletters

| Actor | What you get | Price |
|---|---|---|
| [YouTube Transcript Scraper](https://apify.com/architekture/youtube-transcript-scraper) | YouTube transcript API for captions, subtitles and translations. | $4.00 / 1,000 · Transcript |
| [YouTube & TikTok Transcript Scraper](https://apify.com/architekture/unified-transcript-api) | Extract YouTube and TikTok transcripts, captions and subtitles in mixed URL batches. | $1.00 / 1,000 · Transcript |
| [Threads Replies Scraper](https://apify.com/architekture/threads-replies-scraper) | Export accessible replies to public Threads posts without logging in: text, authors, likes and nesting, plus root posts. | $2.50 / 1,000 · Reply |
| [Substack Scraper](https://apify.com/architekture/substack-scraper) | Substack newsletter scraper (substack.com and custom domains): posts, authors, likes, comment counts, restacks, word counts, tags,… | $1.00 / 1,000 · Post |
| [Facebook Ad Library Scraper](https://apify.com/architekture/ad-intelligence-watchlist) | Track new and changed Facebook and Instagram ads from Meta Ad Library by advertiser and country. | $1.50 / 1,000 · New or changed ad |

### Search, travel and trends

| Actor | What you get | Price |
|---|---|---|
| [Google Trends Scraper](https://apify.com/architekture/google-trends-scraper) | Google Trends Trending Now searches by country from trends.google.com: title, approximate traffic, start time, active flag and related… | $1.00 / 1,000 · Delivered Trending Now row |
| [Google Hotels Scraper](https://apify.com/architekture/google-hotels-scraper) | Extract Google Hotels properties, dated prices, ratings and amenities. | $4.00 / 1,000 · Hotel property |

### Sports

| Actor | What you get | Price |
|---|---|---|
| [Tennis Scraper](https://apify.com/architekture/tennis-data-scraper) | Flashscore tennis (global, flashscore.com): matches, live and final scores, set and tiebreak scores, point-by-point, match statistics,… | $2.50 / 1,000 · Delivered match or ranking |

### Documents

| Actor | What you get | Price |
|---|---|---|
| [EU E-Invoice Parser](https://apify.com/architekture/docparser-invoice-json) | Parse EU e-invoices to JSON: XRechnung, ZUGFeRD, Factur-X and PEPPOL UBL, as XML or PDFs containing invoice XML. | $2.00 / 1,000 · E-invoice |
<!-- catalog:end -->

<sub>Generated weekly from the public Apify Store listings.</sub>

## Contact

- Email: [north@architek.earth](mailto:north@architek.earth)
- Something broken or missing? [Open an issue](https://github.com/architek-earth/.github/issues/new) or start a [discussion](https://github.com/architek-earth/.github/discussions).
