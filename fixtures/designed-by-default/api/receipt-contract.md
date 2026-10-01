# Receipt change contract — synthetic fixture, not a live implementation

POST /receipt accepts a booking reference only from an authenticated receptionist authorised
for that booking. The exported receipt is handed to the patient; any public download URL is
unpredictable and expires after seven days. The storage adapter retains export files for seven
days. The cleanup duty has a named operator but no execution or expiry evidence in this review.
No permission bypass is established by this contract alone. Verify implementation, access,
empty/loading/success/error/expired states, retention and cleanup effects before acceptance.
The change affects human and machine interfaces, stored exports, operating duties and visitor
wording; it cannot be accepted from a layout review alone.
