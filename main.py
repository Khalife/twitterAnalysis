# coding: utf-8
if __name__ == '__main__':
	client_args = {
    'proxies': {
        'http': 'http://empweb1.ey.net:8080/',
        'https': 'http://empweb1.ey.net:8443/',
    			}
	}		
	teamName1 = 'France'
	teamName2 = 'Italie'
	nbTweets = 5
	metrics = getMetrics(client_args, teamName1, teamName2, nbTweets);
	pushFireBase(metrics, 'https://boiling-fire-1432.firebaseio.com/', 'tweetAnalysis')
	pdb.set_trace();
	