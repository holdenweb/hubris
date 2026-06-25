# HUBRIS: Helpful Utility to Bring Reporting Into Spreadsheets

o Sources at https://github.com/holdenweb/hubris

This project is an attempt to help organisations that insist on managing
their businesses, or major aspects thereof, using spreadsheets.
Many articles have been written on the limitations of spreadsheet technology.
If you have any doubts then look at the "The Problem with Spreadsheets"
section of this [LinkedIn
article](https://www.linkedin.com/pulse/spreadsheets-inadequate-effective-management--gjsse/).
Some large organisations are now
[providing advice](https://www.gov.uk/guidance/creating-and-sharing-spreadsheets)
— although in many cases better advice might be:
_stop using spreadsheets for that_!

Rather than try to change the way people do business (imagine "If I Ruled the
World" playing softly in the background), HUBRIS is intended to help people utilise
that locked-up data more effectively in simple and easy-to-understand ways
that don't affect existing workflows.

It lets you add data specifications to any existing spreadsheet. Those
details are then used to extract data from the spreadsheet in JSON, which for
demonstration purposes we inject into simple HTML templates to produce
focused, human-readable output that is easier to digest than raw data in a
spreadsheet.

This is particularly useful for audiences that have an interest in only a
limited number of features from a possibly quite large spreadsheet.

More generally, JSON is such a widely used format that spreadsheet data can
be re-used in a wide range of systems as appropriate.