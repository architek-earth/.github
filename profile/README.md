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
**27 live actors.** Prices are per delivered result; status rows are free.

### Grocery and retail prices

| Actor | What you get | Price |
|---|---|---|
| [Woolworths AU Scraper](https://apify.com/architekture/woolworths-au-product-scraper) | Collect Woolworths Australia prices, specials, unit prices and barcodes, with optional ingredients and nutrition. | $1.50 / 1,000 · Product |
| [Coles AU Scraper](https://apify.com/architekture/coles-au-product-scraper) | Search Coles Australia products, browse categories and specials, or request product details. | $1.50 / 1,000 · Product |
| [ALDI AU Scraper](https://apify.com/architekture/aldi-au-product-scraper) | Search ALDI Australia by keyword, category or SKU. | $1.50 / 1,000 · Product |
| [Woolworths NZ Product & Price Scraper](https://apify.com/architekture/woolworths-nz-scraper) | Extract products, prices, specials and Everyday Rewards club prices from Woolworths New Zealand (formerly Countdown). | $1.00 / 1,000 · Product |
| [New World NZ Scraper](https://apify.com/architekture/new-world-nz-scraper) | Compare New World New Zealand product prices by store: shelf prices, Clubcard offers, unit prices and promotions. | $4.00 / 1,000 · Product + $0.15 per collection delivered |
| [Pak'nSave NZ Scraper](https://apify.com/architekture/paknsave-nz-scraper) | Extract store-scoped Pak’nSave NZ products, NZD prices, unit prices and promotions. | $4.00 / 1,000 · Product + $0.15 per collection delivered |
| [Tesco UK Scraper](https://apify.com/architekture/tesco-uk-scraper) | Search Tesco UK prices, Clubcard offers, unit prices and barcodes. | $2.00 / 1,000 · Product |
| [Sainsbury's UK Scraper](https://apify.com/architekture/sainsburys-uk-scraper) | Search Sainsbury's UK products for prices, unit prices, offers and EAN barcodes. | $2.00 / 1,000 · Product |
| [ALDI Ireland Product Scraper](https://apify.com/architekture/aldi-ie-scraper) | Search ALDI Ireland products by keyword, category or SKU: EUR prices, was-prices, unit prices and Specialbuys dates. | $1.00 / 1,000 · Product |
| [Dunnes Stores Scraper](https://apify.com/architekture/dunnes-ie-scraper) | Search Dunnes Stores Ireland fashion and home products or browse categories. | $1.00 / 1,000 · Product |
| [Mercadona Scraper](https://apify.com/architekture/mercadona-es-scraper) | Extract Mercadona Spain products by keyword, category or product URL: EUR prices, unit prices and category paths. | $1.00 / 1,000 · Product |

### E-commerce and marketplaces

| Actor | What you get | Price |
|---|---|---|
| [Shopify Products Scraper](https://apify.com/architekture/shopify-products-scraper) | Extract Shopify catalogs and collections from accessible public product feeds: prices, sale prices, SKUs and variant availability. | $0.50 / 1,000 · Product |
| [TikTok Shop Scraper](https://apify.com/architekture/tiktok-shop-products-scraper) | Collect public US TikTok Shop products, prices, sellers, ratings and variants. | $3.00 / 1,000 · Product |
| [AliExpress Search Scraper](https://apify.com/architekture/aliexpress-search-scraper) | Search AliExpress by keyword: prices, discounts, order counts, ratings, sponsored flags and delivery estimates. | $2.50 / 1,000 · Product |

### Jobs, companies and people

| Actor | What you get | Price |
|---|---|---|
| [Indeed Scraper](https://apify.com/architekture/indeed-scraper) | Search US Indeed jobs by keyword and location. | $3.50 / 1,000 · Job |
| [LinkedIn Jobs Scraper](https://apify.com/architekture/linkedin-jobs-monitor) | Public LinkedIn jobs with descriptions, salary evidence and saved continuation. | $4.00 / 1,000 · Delivered job |
| [LinkedIn People Scraper](https://apify.com/architekture/linkedin-people-search-scraper) | Export LinkedIn names, headlines and locations using your own session. | $3.00 / 1,000 · Profile |
| [Y Combinator Scraper](https://apify.com/architekture/yc-companies-scraper) | Search the Y Combinator startup directory by keyword, batch, industry and region. | $2.00 / 1,000 · Company |

### Video, social and newsletters

| Actor | What you get | Price |
|---|---|---|
| [YouTube Transcript Scraper](https://apify.com/architekture/youtube-transcript-scraper) | YouTube transcript API for captions, subtitles and translations. | $4.00 / 1,000 · Transcript |
| [YouTube & TikTok Transcript Scraper](https://apify.com/architekture/unified-transcript-api) | Extract YouTube and TikTok transcripts, captions and subtitles in mixed URL batches. | $1.00 / 1,000 · Transcript |
| [Threads Replies Scraper](https://apify.com/architekture/threads-replies-scraper) | Export accessible replies to public Threads posts without logging in: text, authors, likes and nesting, plus root posts. | $2.50 / 1,000 · Reply |
| [Substack Scraper](https://apify.com/architekture/substack-scraper) | Scrape any Substack publication (subdomain or custom domain): post archive with title, authors, tags, likes, comments, restacks, word… | $1.00 / 1,000 · Post |
| [Facebook Ad Library Scraper](https://apify.com/architekture/ad-intelligence-watchlist) | Track new and changed Facebook and Instagram ads from Meta Ad Library by advertiser and country. | $1.50 / 1,000 · New or changed ad |

### Search, travel and trends

| Actor | What you get | Price |
|---|---|---|
| [Google Trends Trending Now Scraper](https://apify.com/architekture/google-trends-scraper) | Collect Google Trending Now titles, approximate traffic, start times and related queries by country. | $1.00 / 1,000 · Delivered Trending Now row |
| [Google Hotels Scraper](https://apify.com/architekture/google-hotels-scraper) | Extract Google Hotels properties, dated prices, ratings and amenities. | $4.00 / 1,000 · Hotel property |

### Sports

| Actor | What you get | Price |
|---|---|---|
| [Tennis Scraper](https://apify.com/architekture/tennis-data-scraper) | Extract Flashscore tennis matches, point-by-point history, statistics, odds and ATP/WTA rankings. | $2.50 / 1,000 · Delivered match or ranking |

### Documents

| Actor | What you get | Price |
|---|---|---|
| [EU E-Invoice Parser](https://apify.com/architekture/docparser-invoice-json) | Parse EU e-invoices to JSON: XRechnung, ZUGFeRD, Factur-X and PEPPOL UBL, as XML or PDFs containing invoice XML. | $2.00 / 1,000 · E-invoice |
<!-- catalog:end -->

<sub>Generated weekly from the public Apify Store listings.</sub>

## Contact

- Email: [north@architek.earth](mailto:north@architek.earth)
- Something broken or missing? [Open an issue](https://github.com/architek-earth/.github/issues/new) or start a [discussion](https://github.com/architek-earth/.github/discussions).
