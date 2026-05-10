# taiwan-places

- no viewing or observational platforms, there are simply too many. rather mark the mountain, beach or whatever

# taiwan-events

- Acceptable events:
  - Both free and paid events are fine
  - Including but not limited to sports, arts, shows, performances, festivals
  - Must be a time limited event with clear start and end dates (one day only, multiple individual days and longer time spans like weeks or months, all are fine)
- Unwanted events:
  - Don't include movies in cinema (too many and unclear timespan)
  - Don't include purely promotional events (like free pizza in a restaurant). This is flexible.
- Required information:
  - at least one title (either English or Chinese)
  - date or dates
  - location (both specific venues and general areas are acceptable, depending on the situation)
  - at least one online source (login required is fine, but the account must be free)
- Titles:
  - both the English and the Chinese title should be official titles, eg. from the official website, promotional material or ticket websites. Translations (either custom ones, or those which come from websites using machine translation) are acceptable if no official ones can be found. They should be marked with `{ut}` (for unofficial translation) at the end of the title.
  - additional titles can be added in a `aka: ...` field, which should come immediately after the title header
- Dates:
  - a single date (`- YYYY-MM-DD`) with optional times (`- YYYY-MM-DD HH:mm`) or time ranges (`- YYYY-MM-DD HH:mm to HH:mm`)
  - a date range (`- YYYY-MM-DD to YYYY-MM-DD`)
  - a date range with times (`- YYYY-MM-DD HH:mm to YYYY-MM-DD HH:mm`)
  - different types can be mixed in one list (`- YYYY-MM-DD, YYYY-MM-DD HH:mm, YYYY-MM-DD to YYYY-MM-DD`)
- Locations:
  - Single and multiple plain-text locations (separated by comma) are supported: `- Location: Taipei City`, `- Location: Taipei City, New Taipei City`
  - Single and multiple linked locations are supported too: `- Location: [Venue A](https://...)`, `- Location: [Venue A](https://...), [Venue B](https://...)`
  - Mixed plain text and links are not supported.

# taiwan-abandoned-places

- 3 categories:
  - abandoned: fully or mostly abandoned places
  - haunted: not or slightly abandoned places included for historical backstory or simply eerie atmosphere
  - destroyed: abandoned places with verifiable information available, which have since been destroyed
- Information which should be included: GPS location, name and type of the place, link to photos or further information. Not all information can always be found. For example these are not enough:
  - gps only (at least one bit of information is necessary like name, photos, type of places like factory or apartment building)
  - photos only (at least the general location like city and district or some approximate location must be given)

# taiwan-tea

- include every type of take-away tea shop
- dine-in restaurants or cafés can be included if they offer primarily tea or a good selection and it's excepted to only order drinks
  - don't include coffee shops which only have a limited amount of tea (especially chain stores)
- don't include shops which only sell tea leaves
