/*Create Table with Aggregatized Parameters*/
CREATE TABLE Accumulo_Aggregatized AS
SELECT DISTINCT SONAR_MEASURES.commitHash, SONAR_ISSUES.creationDate, SONAR_ISSUES.component as component, SONAR_ISSUES.effort as effort,
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
		  			   END) as reliability_Rating, SONAR_MEASURES.developmentCost as development_cost, SONAR_ISSUES.message
FROM SONAR_ISSUES, SONAR_MEASURES
WHERE SONAR_ISSUES.creationCommitHash = SONAR_MEASURES.commitHash AND SONAR_ISSUES.projectID = "accumulo"
ORDER BY component, SONAR_ISSUES.message, SONAR_ISSUES.creationDate