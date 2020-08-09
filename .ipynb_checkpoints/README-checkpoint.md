# US Party Overrepresentation By State

My friend was telling me how both sides were the same when it came to gerrymandering and it triggered me. But rather than just get emotional with the whole dumb situation I decided to do some research. So I collected the data from the below sources and then used a pretty straight forward algorithm to determine if a party is being overrepresented given the state's party percentages.

## Dependencies
1. https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## 2 possibles scenarios:
1. Include 3rd party representation as part of the expected seats (Less Realistic)
2. Exclude 3rd party representation as part of the expected seats (More Realistic)

## Algorithm 1: 
1. Find the share of the remaining seats for each party
	* Dem = Floor(Remaining Seats * PercentDem)
	* Rep = Floor(Remaining Seats * PercentRep)
	* 3rd = Floor(Remaining Seats * Percent3rd)
2. If the above calculations are all equal to 0: (EG 1 seat)
	1. If the remaining seats is at 1, we increment the largest party percentage's seat share
	2. If the remaining seats is at 2, we increment the 2 largest party percentages' seat shares
	3. Else, For each party, if the party percentage is greater than 50%, we increment that party's seat share
3. Else:
	1. Decrement remaining seats by all of the party seat shares
	2. Repeat with the smaller remaining seats
5. Repeat until remaining seats is 0

## Algorithm 2: 
1. Find the share of the remaining seats for each party
	* Dem = Floor(Remaining Seats * PercentDem)
	* Rep = Floor(Remaining Seats * PercentRep)
2. If the above calculations are all equal to 0: (EG 1 seat)
	1. If the remaining seats is at 1, we increment the largest party percentage's seat share
	3. Else, For each party, if the party percentage is greater than 50%, we increment that party's seat share
3. Else:
	1. Decrement remaining seats by all of the party seat shares
	2. Repeat with the smaller remaining seats
5. Repeat until remaining seats is 0

## Sources
* Source For Party Affiliation Percents:
  * https://en.wikipedia.org/wiki/Political_party_strength_in_U.S._states

* Source For Current Seats For States By Party:
  * https://en.wikipedia.org/wiki/Political_party_strength_in_U.S._states
  * Since Wikipedia is dynamic, I pulled the data on 08/08/2020 if there is an archive somewhere

Note: The reason I included the dumb tabs ("\t") is so I could copy and paste it into the sheets with ease. Lazy on my part but w/e