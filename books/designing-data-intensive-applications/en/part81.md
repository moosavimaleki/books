![ddia 0202](assets/ddia_0202.png) ###### Figure 2-2. One-to-many relationships forming a tree structure. ## Many-to-One and Many-to-Many Relationships In [Example 2-1](#fig_billgates_json) in the preceding section, region_id and industry_id are given as IDs,
not as plain-text strings "Greater Seattle Area" and "Philanthropy". Why? 
If the user interface has free-text fields for entering the region and the industry, it makes sense
to store them as plain-text strings. But there are advantages to having standardized lists of
geographic regions and industries, and letting users choose from a drop-down list or autocompleter: *  Consistent style and spelling across profiles *  Avoiding ambiguity (e.g., if there are several cities with the same name) *  Ease of updating—the name is stored in only one place, so it is easy to update across the board if
it ever needs to be changed (e.g., change of a city name due to political events) *  Localization support—when the site is translated into other languages, the standardized lists can
be localized, so the region and industry can be displayed in the viewer’s language