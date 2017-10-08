`
----- Stating Verification Tasks -----
...............................................................................................................................
# compliance_reports : Generate report content ****************************************************************************
  * LAB-COR2                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR4                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR1                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE1                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR3                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE2                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE3                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE4                    - yellowchanged=True -- yellow -----------------------------------------------
# compliance_reports : Assemble full reports ******************************************************************************
  * LAB-COR1                   - yellowchanged=True -- yellowOK ---------------------------------------------
  * LAB-COR2                   - yellowchanged=True -- yellowOK ---------------------------------------------
  * LAB-COR3                   - yellowchanged=True -- yellowOK ---------------------------------------------
  * LAB-COR4                   - yellowchanged=True -- yellowOK ---------------------------------------------
  * LAB-PE1                    - yellowchanged=True -- yellowOK ---------------------------------------------
  * LAB-PE2                    - yellowchanged=True -- yellowOK ---------------------------------------------
  * LAB-PE3                    - yellowchanged=True -- yellowOK ---------------------------------------------
  * LAB-PE4                    - yellowchanged=True -- yellowOK ---------------------------------------------
........................................................
# compliance_reports : Create the aggregated report ***********************************************************************
  * LAB-COR1                   - yellowchanged=True -- yellowOK ---------------------------------------------
................

# STATS *******************************************************************************************************************
yellowLAB-COR1    : ok=41       changed=13      failed=0        unreachable=0
yellowLAB-COR2    : ok=33       changed=11      failed=0        unreachable=0
yellowLAB-COR3    : ok=33       changed=11      failed=0        unreachable=0
yellowLAB-COR4    : ok=33       changed=11      failed=0        unreachable=0
yellowLAB-PE1    : ok=33        changed=11      failed=0        unreachable=0
yellowLAB-PE2    : ok=33        changed=11      failed=0        unreachable=0
yellowLAB-PE3    : ok=33        changed=11      failed=0        unreachable=0
yellowLAB-PE4    : ok=33        changed=11      failed=0        unreachable=0

----- Checking reports/*.txt for '[FAIL]' items -----
reports/LAB-COR1.txt:IS-IS Adjancency                                  Check for IS-IS neighbour on 'em0'                                         [FAIL]
reports/LAB-COR1.txt:Ping Test                                         Check for successful ping to 169.254.0.29                                  [FAIL]
reports/LAB-COR4.txt:IS-IS Adjancency                                  Check for IS-IS neighbour on 'em0'                                         [FAIL]
reports/LAB-COR4.txt:Ping Test                                         Check for successful ping to 169.254.0.28                                  [FAIL]

----- End of script -----
`