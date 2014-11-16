def calculateSimilarItems(prefs,n=10):
  # Create a dictionary of items showing which other items they
  # are most similar to.
  result={}
  item1 = 'Top Gun (1986)'
  # Invert the preference matrix to be item-centric
  itemPrefs=transformPrefs(prefs)
  c=0
  for item in itemPrefs:
    # Status updates for large datasets
    # c+=1
    # if c%100==0: print "%d / %d" % (c,len(itemPrefs))
    # Find the most similar items to this one       
    scores=topMatches(itemPrefs,item1,n=n,similarity=sim_pearson)
    result[item]=scores
  return result


def loadMovieLens():
  # Get movie titles
  readData = open('/home/bbokka/cs594/A8/u.data', 'r')
  readItem = open('/home/bbokka/cs594/A8/u.item','r')
  movies={}
  for line in readItem:    
    (id,title)=line.split('|')[0:2] 
    movies[id]=title  
  # Load data
  prefs={}
  for line in readData:
    (user,movieid,rating,ts)=line.split('\t')
    prefs.setdefault(user,{})
    prefs[user][movies[movieid]]=float(rating)
  
  return prefs

  # To get the negative corelation line 42 is commented.
  def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  #scores.reverse()
  return scores[0:n]