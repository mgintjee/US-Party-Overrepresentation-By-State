#####################################
## TBD YO ##
## Created On: 07.17.19            ## 
## Updated On: 07.17.19            ##
#####################################

import HoRWikiInformationExtraction, GallupPollInformationExtraction

def main():
    HoRWikiInformation = HoRWikiInformationExtraction.ExtractInfoFromHoRWiki()
    GallupPollInformation = GallupPollInformationExtraction.ExtractInfoFromGallupPoll()
    CommonStates = []
    print(GallupPollInformation.keys())
    print(HoRWikiInformation.keys())
    for state in GallupPollInformation.keys():
        if(state in HoRWikiInformation.keys()):
            CommonStates.append(state)
            
    print(CommonStates)

    for state in CommonStates:
        print(state)
        HoRWikiInformation[state].ToString()
        GallupPollInformation[state].ToString()
    

if __name__=="__main__":
    main()
