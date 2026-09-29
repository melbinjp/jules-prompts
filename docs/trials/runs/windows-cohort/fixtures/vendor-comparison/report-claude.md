The decision isn't finished, because it needs the station manager's yes. What I could do is show that D0003 (CloudA) was wrong and write up CloudB as a proposal, D0004, for approval. Nothing was bought, published or sent.

CloudA fails the $60 limit. D0003 entered transfer as 5 GB instead of 5,000 GB, so it showed $23.45 a month. At 1,000 GB stored and 5,000 GB downloaded, CloudA costs $473.00 a month; it only fits $60 if downloads stay under about 411 GB a month.

CloudB fits, with little room: $55.00 a month at today's size. That holds only while downloads stay at or under 5,500 GB a month, and storage alone reaches about $60 around 1,700 GB (roughly year 7). D0004 sets reopen triggers well before that: an invoice above $57, downloads above 5,300 GB, or storage past 1,600 GB.

Other faults in D0003:
- Marked as a reversible choice, but CloudA's standard tier has no custom domain, so every feed and blog link would be stuck on CloudA's hostname.
- Its evidence was CloudA's own marketing page and a 2 MB upload from the office.
- It scored popularity and developer experience, which serve none of the project's success measures.
- It compared only two options and had no approver.

Proposal D0004 (status proposed): use CloudB, served only through a domain the station controls, so the storage can move later without changing any link; the studio NAS holds the second copy. A choice this hard to reverse needs two different kinds of evidence; I have a calculation and the stored price lists but not the real download figure or a test upload, so it stays a proposal.

Assumptions recorded for the owner: the 1,000 GB is the served MP3 copy (if it is FLAC masters CloudB would cost about $50.83; if MP3, the FLAC masters (about 6,076 GB) will not fit the NAS's 4,000 GB); the 5,000 GB a month download figure is measured, not guessed; the station controls a domain; the price lists carry no retrieval date or URL and could not be rechecked without the network.

D0002 (serve MP3, keep FLAC) left accepted; I reproduced its listening-test counts. The cost calculation was run in Docker and exited 0.

Verified 5 of 8 items: the CloudA cost, the CloudB cost, the CloudB sensitivity limits, the D0002 counts, the D0003 faults. Not verified: live prices, real traffic, CloudB's terms on how stored volume is counted, its export and data-ownership terms. Not evaluated: serving straight from the NAS.
