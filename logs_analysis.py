import psycopg2

def connection(ques):
	db=psycopg2.connect(dbname="news")
	c=db.cursor()
	c.execute(ques)
	line=c.fetchall()
	db.close()
	return line

def popular_articles():
     ques="""select articles.title as topic ,count(*) as number from articles,log 
        where log.path=concat('/article/',articles.slug) group by topic
        order by number desc limit 3;"""
       
     Answer1=connection(ques)
     print('\nTHE MOST POPULAR THREE ARTICLES OF ALL TIME ARE:')
     for i in Answer1:
       print('"'+i[0] +'"' ' -- ' + str(i[1]) + " views")
      
def popular_authors():
     ques="""select authors.name as name,COUNT(*) as number from authors , articles , log
        where authors.id = articles.author and log.path = concat('/article/', articles.slug)
        group by name order by number desc limit 3;"""
     Answer2 = connection(ques)
     print('\nTHE MOST POPULARAR ARTICLES AUTHORS OF ALL TIME ARE:')
     for i in Answer2:
        print(i[0] + ' -- ' + str(i[1]) + " views")
        
        
def errors():
    ques = """
        select total.date,((t.error*1.0) / total.requests) as percent
        from (select date_trunc('day', time) as date, count(*) as error
        from log where status = '404 NOT FOUND' group by date) as t , (select date_trunc('day', time) as date, count(*) as requests from log group by date)as total
        where total.date = t.date and( (t.error*1.0) / total.requests) > 0.01
        order by percent desc;
    """

    Answer3 = connection(ques)
    print('\nTHE DAY ON WHICH MORE THAN 1% OF REQUEST LEAD TO ERRORS IS:')
    for i in Answer3:
        error_count = str(round(i[1]*100, 1)) + "% errors" 
        print(i[0].strftime('%b %d, %Y') + " -- " + error_count)
                
popular_articles()
popular_authors()
errors()
