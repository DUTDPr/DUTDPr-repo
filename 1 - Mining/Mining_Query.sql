/**Version 2.01*/
/* current target="org.apache:cocoon"

/*Count total number of issues in Sonar_issues*/
select PROJECT_ID, count(*) AS issues from SONAR_ISSUES GROUP by PROJECT_ID ORDER by issues desc

/*Select issues from project X*/
select * from SONAR_ISSUES where PROJECT_ID = "X"

/*Count total issues of project X group by by creation date*/
select CREATION_DATE , count(*) from SONAR_ISSUES where PROJECT_ID = 'X' group by CREATION_DATE order by CREATION_DATE asc

/*Select commit from project X*/
select * from GIT_COMMITS where PROJECT_ID = "X"

/*Select measures from project X*/
select * from SONAR_MEASURES where PROJECT_ID = "X"

/*2nd Contributions*/

/*Show Processed Issues List*/
SELECT DISTINCT SONAR_ISSUES.CREATION_ANALYSIS_KEY, SONAR_ISSUES.CREATION_DATE, SONAR_ISSUES.COMPONENT as COMPONENT, SONAR_ISSUES.EFFORT, SONAR_ISSUES.TYPE, SONAR_ISSUES.TAGS,
                        (CASE 
						WHEN SONAR_ISSUES.SEVERITY = 'INFO' THEN '0.1'
						WHEN SONAR_ISSUES.SEVERITY = 'MINOR' THEN '0.2'
						WHEN SONAR_ISSUES.SEVERITY = 'MAJOR' THEN '0.4'	
						WHEN SONAR_ISSUES.SEVERITY = 'CRITICAL' THEN '0.6'
						WHEN SONAR_ISSUES.SEVERITY = 'BLOCKER' THEN '0.8' 
					   END) as SEVERITY, 
                       (CASE 
						WHEN SONAR_MEASURES.SQALE_RATING = '5' THEN '0.05'
						WHEN SONAR_MEASURES.SQALE_RATING = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.SQALE_RATING = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.SQALE_RATING = '2' THEN '0.5'
						WHEN SONAR_MEASURES.SQALE_RATING = '1' THEN '1'
		  			   END) as maintainability_Rating,
                       (CASE 
						WHEN SONAR_MEASURES.SECURITY_RATING = '5' THEN '0.05'
						WHEN SONAR_MEASURES.SECURITY_RATING = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.SECURITY_RATING = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.SECURITY_RATING = '2' THEN '0.5'
						WHEN SONAR_MEASURES.SECURITY_RATING = '1' THEN '1'
		  			   END) as security_Rating, 
                        (CASE 
						WHEN SONAR_MEASURES.RELIABILITY_RATING = '5' THEN '0.05'
						WHEN SONAR_MEASURES.RELIABILITY_RATING = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.RELIABILITY_RATING = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.RELIABILITY_RATING = '2' THEN '0.5'
						WHEN SONAR_MEASURES.RELIABILITY_RATING = '1' THEN '1'
		  			   END) as RELIABILITY_RATING, SONAR_MEASURES.DEVELOPMENT_COST as DEVELOPMENT_COST
FROM SONAR_ISSUES, SONAR_MEASURES
WHERE SONAR_ISSUES.CREATION_ANALYSIS_KEY = SONAR_MEASURES.ANALYSIS_KEY and SONAR_ISSUES.PROJECT_ID = "x"

/**Version 1.0**/
/* current target="Accumulo"

/*Count total number of issues in Sonar_issues*/
select projectID, count(*) AS issues from SONAR_ISSUES GROUP by projectID ORDER by issues desc

/*Select issues from project X*/
select * from SONAR_ISSUES where projectID = "X"

/*Select unique issues from project X*/
select distinct * from SONAR_ISSUES where projectID = "X"

/*Count total issues of project X group by by creation date*/
select creationDate , count(*) from SONAR_ISSUES where projectID = 'x' group by creationDate order by creationDate asc

/*Select commit from project X*/
select * from GIT_COMMITS where projectID = "X"

/*Select measures from project X*/
select * from SONAR_MEASURES where projectID = "X"

/*2nd Contributions*/

/*Show Processed Issues List*/
SELECT DISTINCT SONAR_MEASURES.commitHash, SONAR_ISSUES.creationDate, SONAR_ISSUES.projectID as project_name, SONAR_ISSUES.component as component, SONAR_ISSUES.effort, SONAR_ISSUES.type,
                        (CASE 
						WHEN SONAR_ISSUES.severity = 'INFO' THEN '0.1'
						WHEN SONAR_ISSUES.severity = 'MINOR' THEN '0.2'
						WHEN SONAR_ISSUES.severity = 'MAJOR' THEN '0.4'	
						WHEN SONAR_ISSUES.severity = 'CRITICAL' THEN '0.6'
						WHEN SONAR_ISSUES.severity = 'BLOCKER' THEN '0.8' 
					   END) as severity, 
                       (CASE 
						WHEN SONAR_MEASURES.sqaleRating = '5' THEN '0.05'
						WHEN SONAR_MEASURES.sqaleRating = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.sqaleRating = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.sqaleRating = '2' THEN '0.5'
						WHEN SONAR_MEASURES.sqaleRating = '1' THEN '1'
		  			   END) as maintainability_Rating,
                       (CASE 
						WHEN SONAR_MEASURES.securityRating = '5' THEN '0.05'
						WHEN SONAR_MEASURES.securityRating = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.securityRating = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.securityRating = '2' THEN '0.5'
						WHEN SONAR_MEASURES.securityRating = '1' THEN '1'
		  			   END) as security_Rating, 
                        (CASE 
						WHEN SONAR_MEASURES.reliabilityRating = '5' THEN '0.05'
						WHEN SONAR_MEASURES.reliabilityRating = '4' THEN '0.1'
					    WHEN SONAR_MEASURES.reliabilityRating = '3' THEN '0.2'	
						WHEN SONAR_MEASURES.reliabilityRating = '2' THEN '0.5'
						WHEN SONAR_MEASURES.reliabilityRating = '1' THEN '1'
		  			   END) as reliability_Rating, SONAR_MEASURES.developmentCost as development_cost
FROM SONAR_ISSUES, SONAR_MEASURES
WHERE SONAR_ISSUES.creationCommitHash = SONAR_MEASURES.commitHash