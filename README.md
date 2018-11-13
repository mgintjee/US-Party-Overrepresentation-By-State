# US Party Overrepresentation By State

My friend was telling me how both sides were the same when it came to gerrymandering and it triggered me. But rather than just get emotional with the whole dumb situation I decided to do some research. So I collected the data from the below sources and then used a pretty straight forward algorithm to determine if a party is being overrepresented given the state's party percentages.

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

## Outcome 1:
* Democrats   Overrepresented in **13 states**: CA, CT, IL, MD, MA, MN, NV, NH, NJ, NY, OR, RI, WA
* Republicans Overrepresented in **30 states**: AL, AZ, AR, CO, FL, GA, IL, IN, IA, KS, KY, LA, MI, MS, MO, NE, NJ, NY, NC, OH, OK, PA, SC, TN, TX, UT, VA, WV, WI, US
* Both        Overrepresented in  **3 states**: IL, NJ, NY 
* [Google Sheets](https://docs.google.com/spreadsheets/d/1e9mlfr3_OIc8v5Oabc0wPBVADV7ZabuXLx_Us7ock8M/edit#gid=1130096001)

## Outcome 2:
* Democrats   Overrepresented in **8 states**: CA, CT, MD, MA, NV, NH, OR, RI
* Republicans Overrepresented in **28 states**: AL, AR, CO, FL, GA, IL, IN, IA, KS, KY, LA, MI, MS, MO, NE, NY, NC, OH, OK, PA, SC, TN, TX, UT, VA, WV, WI, US
* Both        Overrepresented in  **0 states**: null
* [Google Sheets](https://docs.google.com/spreadsheets/d/1e9mlfr3_OIc8v5Oabc0wPBVADV7ZabuXLx_Us7ock8M/edit#gid=0)

## Sources
* Source For Party Affiliation Percents:
  * https://news.gallup.com/poll/226643/2017-party-affiliation-state.aspx

* Source For Current Seats For States By Party:
  * https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives
  * Since Wikipedia is dynamic, I pulled the data on 11/12/2018 if there is an archive somewhere

Note: The reason I included the dumb tabs ("\t") is so I could copy and paste it into the sheets with ease. Lazy on my part but w/e