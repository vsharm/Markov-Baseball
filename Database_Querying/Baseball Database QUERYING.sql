SET @OUTS = 2;
SET @BASES = 7;

/********************************************************/

SELECT COUNT(*) FROM `events` WHERE OUTS_CT=@OUTS 
						 AND START_BASES_CD=@BASES
						 INTO @TOTAL_EVENTS;

SELECT SUM(EVENT_RUNS_CT) FROM `events` WHERE OUTS_CT=@OUTS
								   AND START_BASES_CD=@BASES
								   INTO @SUM_RUNS;

SET @Percentage = @SUM_RUNS/ @TOTAL_EVENTS;
SELECT @Percentage;

