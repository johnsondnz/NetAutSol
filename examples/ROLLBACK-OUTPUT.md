`
----- Rolling Back Configurations -----
...........
# Rollback to rescue configuration ****************************************************************************************
  * LAB-PE1                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR1                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR3                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR4                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR2                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE2                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE3                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE4                    - yellowchanged=True -- yellow -----------------------------------------------
# Remove Old Configuration ************************************************************************************************
  * LAB-COR1                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-COR2                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-COR4                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-COR3                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-PE1                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-PE2                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-PE3                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-PE4                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}

# STATS *******************************************************************************************************************
yellowLAB-COR1    : ok=6        changed=1       failed=0        unreachable=0
yellowLAB-COR2    : ok=3        changed=1       failed=0        unreachable=0
yellowLAB-COR3    : ok=3        changed=1       failed=0        unreachable=0
yellowLAB-COR4    : ok=3        changed=1       failed=0        unreachable=0
yellowLAB-PE1    : ok=3 changed=1       failed=0        unreachable=0
yellowLAB-PE2    : ok=3 changed=1       failed=0        unreachable=0
yellowLAB-PE3    : ok=3 changed=1       failed=0        unreachable=0
yellowLAB-PE4    : ok=3 changed=1       failed=0        unreachable=0

----- End of script -----
`