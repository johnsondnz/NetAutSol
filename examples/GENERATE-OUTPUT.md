```
----- Generating Configurations -----
...........................
# Remove Old Configuration ************************************************************************************************
  * LAB-COR2                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-COR1                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-COR3                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-COR4                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-PE1                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-PE2                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-PE3                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
  * LAB-PE4                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'directory', u'absent')}
# Create Empty Build Directory ********************************************************************************************
  * LAB-COR1                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'absent', u'directory')}
  * LAB-COR2                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'absent', u'directory')}
  * LAB-COR4                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'absent', u'directory')}
  * LAB-COR3                   - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'absent', u'directory')}
  * LAB-PE2                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'absent', u'directory')}
  * LAB-PE3                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'absent', u'directory')}
  * LAB-PE1                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'absent', u'directory')}
  * LAB-PE4                    - greenchanged=False -- green ------------------------------------------------
    yellow{u'state': (u'absent', u'directory')}
# config_base : Create base configs for nodes *****************************************************************************
  * LAB-COR4                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE1                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR3                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR1                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-COR2                   - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE2                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE3                    - yellowchanged=True -- yellow -----------------------------------------------
  * LAB-PE4                    - yellowchanged=True -- yellow -----------------------------------------------
# config_fabric : Configure MPLS fabric ***********************************************************************************
  * LAB-COR4                   - yellowchanged=True -- yellowAll items completed ----------------------------
      * {u'right_port': u'em1', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR3', u'left_port': u'em1', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR4', u'left_port': u'em1', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR3', u'left_port': u'em2', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR2', u'left_port': u'em3', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR4', u'left_port': u'em5', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR3', u'left_port': u'em4', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR3', u'left_port': u'em5', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR4', u'left_port': u'em4', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-COR3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em0', u'right': u'LAB-COR4', u'left_port': u'em0', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
  * LAB-COR1                   - yellowchanged=True -- yellowAll items completed ----------------------------
      * {u'right_port': u'em1', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR3', u'left_port': u'em1', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR4', u'left_port': u'em1', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR3', u'left_port': u'em2', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR2', u'left_port': u'em3', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR4', u'left_port': u'em5', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR3', u'left_port': u'em4', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR3', u'left_port': u'em5', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR4', u'left_port': u'em4', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-COR3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em0', u'right': u'LAB-COR4', u'left_port': u'em0', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
  * LAB-COR2                   - yellowchanged=True -- yellowAll items completed ----------------------------
      * {u'right_port': u'em1', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR3', u'left_port': u'em1', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR4', u'left_port': u'em1', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR3', u'left_port': u'em2', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR2', u'left_port': u'em3', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR4', u'left_port': u'em5', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR3', u'left_port': u'em4', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR3', u'left_port': u'em5', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR4', u'left_port': u'em4', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-COR3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em0', u'right': u'LAB-COR4', u'left_port': u'em0', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
  * LAB-COR3                   - yellowchanged=True -- yellowAll items completed ----------------------------
      * {u'right_port': u'em1', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR3', u'left_port': u'em1', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR4', u'left_port': u'em1', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR3', u'left_port': u'em2', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR2', u'left_port': u'em3', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR4', u'left_port': u'em5', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR3', u'left_port': u'em4', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR3', u'left_port': u'em5', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR4', u'left_port': u'em4', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-COR3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em0', u'right': u'LAB-COR4', u'left_port': u'em0', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
  * LAB-PE1                    - yellowchanged=True -- yellowAll items completed ----------------------------
      * {u'right_port': u'em1', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR3', u'left_port': u'em1', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR4', u'left_port': u'em1', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR3', u'left_port': u'em2', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR2', u'left_port': u'em3', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR4', u'left_port': u'em5', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR3', u'left_port': u'em4', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR3', u'left_port': u'em5', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR4', u'left_port': u'em4', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-COR3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em0', u'right': u'LAB-COR4', u'left_port': u'em0', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
  * LAB-PE2                    - yellowchanged=True -- yellowAll items completed ----------------------------
      * {u'right_port': u'em1', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR3', u'left_port': u'em1', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR4', u'left_port': u'em1', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR3', u'left_port': u'em2', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR2', u'left_port': u'em3', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR4', u'left_port': u'em5', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR3', u'left_port': u'em4', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR3', u'left_port': u'em5', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR4', u'left_port': u'em4', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-COR3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em0', u'right': u'LAB-COR4', u'left_port': u'em0', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
  * LAB-PE3                    - yellowchanged=True -- yellowAll items completed ----------------------------
      * {u'right_port': u'em1', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR3', u'left_port': u'em1', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR4', u'left_port': u'em1', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR3', u'left_port': u'em2', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR2', u'left_port': u'em3', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR4', u'left_port': u'em5', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR3', u'left_port': u'em4', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR3', u'left_port': u'em5', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR4', u'left_port': u'em4', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-COR3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em0', u'right': u'LAB-COR4', u'left_port': u'em0', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
  * LAB-PE4                    - yellowchanged=True -- yellowAll items completed ----------------------------
      * {u'right_port': u'em1', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR1', u'left_port': u'em1', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR2', u'left_port': u'em2', u'left': u'LAB-PE2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR3', u'left_port': u'em1', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-PE3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR4', u'left_port': u'em1', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em4', u'right': u'LAB-COR3', u'left_port': u'em2', u'left': u'LAB-PE4'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em3', u'right': u'LAB-COR2', u'left_port': u'em3', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR4', u'left_port': u'em5', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR3', u'left_port': u'em4', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em5', u'right': u'LAB-COR3', u'left_port': u'em5', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em1', u'right': u'LAB-COR4', u'left_port': u'em4', u'left': u'LAB-COR2'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em2', u'right': u'LAB-COR4', u'left_port': u'em2', u'left': u'LAB-COR3'}- redFAILED!!! -- red ---------
      * {u'right_port': u'em0', u'right': u'LAB-COR4', u'left_port': u'em0', u'left': u'LAB-COR1'}- redFAILED!!! -- red ---------
................
# Executing Napalm Tasks **************************************************************************************************
  * LAB-PE1                    - yellowchanged=True ----------------------------------------------------
    yellow[edit]
    + groups {
    +     OUT-OF-BAND-MANAGEMENT {
    +         interfaces {
    +             em0 {
    +                 description "OOOB MANAGEMENT INTERFACE --- DO NOT DELETE";
    +                 unit 0 {
    +                     family inet {
    +                         address 192.168.1.1/24;
    +                     }
    +                 }
    +             }
    +         }
    +         routing-options {
    +             static {
    +                 route 0.0.0.0/0 next-hop 192.168.1.237;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-MPLS {
    +         protocols {
    +             mpls {
    +                 log-updown {
    +                     syslog;
    +                     trap;
    +                     trap-path-down;
    +                     trap-path-up;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-RSVP {
    +         protocols {
    +             rsvp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <ge-*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface <em*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface lo0.0 {
    +                     aggregate;
    +                     reliable;
    +                     link-protection;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-LDP {
    +         protocols {
    +             ldp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface lo0.0;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-ISIS {
    +         protocols {
    +             isis {
    +                 reference-bandwidth 10g;
    +                 traffic-engineering {
    +                     family inet {
    +                         shortcuts;
    +                     }
    +                     family inet6 {
    +                         shortcuts;
    +                     }
    +                 }
    +                 interface lo0.0 {
    +                     passive;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <em-*> {
    +                     node-link-protection;
    +                 }
    +             }
    +         }
    +     }
    + }
    + apply-groups OUT-OF-BAND-MANAGEMENT;
    [edit system]
    -  host-name LAB-PE1_bootstrap;
    +  host-name LAB-PE1;
    +  syslog {
    +      user * {
    +          any emergency;
    +      }
    +      file messages {
    +          any notice;
    +          authorization info;
    +      }
    +      file interactive-commands {
    +          interactive-commands any;
    +      }
    +  }
    +  ntp {
    +      boot-server 192.168.1.237;
    +      server 192.168.1.237;
    +  }
    [edit interfaces]
    -   em0 {
    -       description "MANAGEMENT INTERFACE --- DO NOT DELETE";
    -       unit 0 {
    -           family inet {
    -               address 192.168.1.1/24;
    -           }
    -       }
    -   }
    +   /* link_index: 0 | LAB-PE1 em1.0 169.254.0.0/31 --> 169.254.0.1/31 em1.0 LAB-COR1 */
    +   em1 {
    +       description "WAN | LAB-COR1 em1";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.0/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 2 | LAB-PE1 em2.0 169.254.0.2/31 --> 169.254.0.3/31 em1.0 LAB-COR2 */
    +   em2 {
    +       description "WAN | LAB-COR2 em1";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.2/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   lo0 {
    +       unit 0 {
    +           description "PEERING INTERFACE --- DO NOT DELETE";
    +           family inet {
    +               address 10.1.1.1/32;
    +           }
    +           family iso {
    +               address 49.0000.0172.0016.0001.00;
    +           }
    +       }
    +   }
    [edit routing-options]
    -   static {
    -       route 0.0.0.0/0 next-hop 192.168.1.237;
    -   }
    +   router-id 10.1.1.1;
    +   autonomous-system 0.65535;
    +   forwarding-table {
    +       /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +       export load-balancing-policy;
    +   }
    +   dynamic-tunnels {
    +       dt-1 {
    +           rsvp-te rsvp-te-1 {
    +               label-switched-path-template {
    +                   default-template;
    +               }
    +               destination-networks {
    +                   10.1.1.0/24;
    +               }
    +           }
    +       }
    +   }
    [edit]
    +  protocols {
    +      rsvp {
    +          apply-groups PROTOCOL-DEFAULTS-RSVP;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      mpls {
    +          apply-groups PROTOCOL-DEFAULTS-MPLS;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      isis {
    +          apply-groups PROTOCOL-DEFAULTS-ISIS;
    +          interface em1.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em2.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +      }
    +      ldp {
    +          apply-groups PROTOCOL-DEFAULTS-LDP;
    +          keepalive-timeout 180;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      lldp {
    +          interface all;
    +      }
    +  }
    +  /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +  policy-options {
    +      policy-statement load-balancing-policy {
    +          then {
    +              load-balance per-packet;
    +          }
    +      }
    +  }
  * LAB-COR4                   - yellowchanged=True ----------------------------------------------------
    yellow[edit]
    + groups {
    +     OUT-OF-BAND-MANAGEMENT {
    +         interfaces {
    +             em0 {
    +                 description "OOOB MANAGEMENT INTERFACE --- DO NOT DELETE";
    +                 unit 0 {
    +                     family inet {
    +                         address 192.168.1.14/24;
    +                     }
    +                 }
    +             }
    +         }
    +         routing-options {
    +             static {
    +                 route 0.0.0.0/0 next-hop 192.168.1.237;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-MPLS {
    +         protocols {
    +             mpls {
    +                 log-updown {
    +                     syslog;
    +                     trap;
    +                     trap-path-down;
    +                     trap-path-up;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-RSVP {
    +         protocols {
    +             rsvp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <ge-*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface <em*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface lo0.0 {
    +                     aggregate;
    +                     reliable;
    +                     link-protection;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-LDP {
    +         protocols {
    +             ldp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface lo0.0;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-ISIS {
    +         protocols {
    +             isis {
    +                 reference-bandwidth 10g;
    +                 traffic-engineering {
    +                     family inet {
    +                         shortcuts;
    +                     }
    +                     family inet6 {
    +                         shortcuts;
    +                     }
    +                 }
    +                 interface lo0.0 {
    +                     passive;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <em-*> {
    +                     node-link-protection;
    +                 }
    +             }
    +         }
    +     }
    + }
    + apply-groups OUT-OF-BAND-MANAGEMENT;
    [edit system]
    -  host-name LAB-COR4_bootstrap;
    +  host-name LAB-COR4;
    +  syslog {
    +      user * {
    +          any emergency;
    +      }
    +      file messages {
    +          any notice;
    +          authorization info;
    +      }
    +      file interactive-commands {
    +          interactive-commands any;
    +      }
    +  }
    +  ntp {
    +      boot-server 192.168.1.237;
    +      server 192.168.1.237;
    +  }
    [edit interfaces]
    +   /* link_index: 28 | LAB-COR4 em0.0 169.254.0.29/31 --> 169.254.0.28/31 em0.0 LAB-COR1 */
        em0 { ... }
    [edit interfaces em0]
    -   description "MANAGEMENT INTERFACE --- DO NOT DELETE";
    +   description "WAN | LAB-COR1 em0";
    +   mtu 2000;
    [edit interfaces em0 unit 0 family inet]
    +       address 169.254.0.29/31;
    -       address 192.168.1.14/24;
    [edit interfaces em0 unit 0]
    +      family iso;
    +      family mpls;
    [edit interfaces]
    +   /* link_index: 24 | LAB-COR4 em1.0 169.254.0.25/31 --> 169.254.0.24/31 em4.0 LAB-COR2 */
    +   em1 {
    +       description "WAN | LAB-COR2 em4";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.25/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 26 | LAB-COR4 em2.0 169.254.0.27/31 --> 169.254.0.26/31 em2.0 LAB-COR3 */
    +   em2 {
    +       description "WAN | LAB-COR3 em2";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.27/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 12 | LAB-COR4 em3.0 169.254.0.13/31 --> 169.254.0.12/31 em1.0 LAB-PE4 */
    +   em3 {
    +       description "WAN | LAB-PE4 em1";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.13/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 10 | LAB-COR4 em4.0 169.254.0.11/31 --> 169.254.0.10/31 em2.0 LAB-PE3 */
    +   em4 {
    +       description "WAN | LAB-PE3 em2";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.11/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 18 | LAB-COR4 em5.0 169.254.0.19/31 --> 169.254.0.18/31 em5.0 LAB-COR1 */
    +   em5 {
    +       description "WAN | LAB-COR1 em5";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.19/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   lo0 {
    +       unit 0 {
    +           description "PEERING INTERFACE --- DO NOT DELETE";
    +           family inet {
    +               address 10.1.1.14/32;
    +           }
    +           family iso {
    +               address 49.0000.0172.0016.0014.00;
    +           }
    +       }
    +   }
    [edit routing-options]
    -   static {
    -       route 0.0.0.0/0 next-hop 192.168.1.237;
    -   }
    +   router-id 10.1.1.14;
    +   autonomous-system 0.65535;
    +   forwarding-table {
    +       /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +       export load-balancing-policy;
    +   }
    +   dynamic-tunnels {
    +       dt-1 {
    +           rsvp-te rsvp-te-1 {
    +               label-switched-path-template {
    +                   default-template;
    +               }
    +               destination-networks {
    +                   10.1.1.0/24;
    +               }
    +           }
    +       }
    +   }
    [edit]
    +  protocols {
    +      rsvp {
    +          apply-groups PROTOCOL-DEFAULTS-RSVP;
    +          interface em4.0;
    +          interface em3.0;
    +          interface em5.0;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em0.0;
    +      }
    +      mpls {
    +          apply-groups PROTOCOL-DEFAULTS-MPLS;
    +          interface em4.0;
    +          interface em3.0;
    +          interface em5.0;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em0.0;
    +      }
    +      isis {
    +          apply-groups PROTOCOL-DEFAULTS-ISIS;
    +          interface em0.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em1.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em2.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em3.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em4.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em5.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +      }
    +      ldp {
    +          apply-groups PROTOCOL-DEFAULTS-LDP;
    +          keepalive-timeout 180;
    +          interface em0.0;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em3.0;
    +          interface em4.0;
    +          interface em5.0;
    +      }
    +      lldp {
    +          interface all;
    +      }
    +  }
    +  /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +  policy-options {
    +      policy-statement load-balancing-policy {
    +          then {
    +              load-balance per-packet;
    +          }
    +      }
    +  }
  * LAB-COR1                   - yellowchanged=True ----------------------------------------------------
    yellow[edit]
    + groups {
    +     OUT-OF-BAND-MANAGEMENT {
    +         interfaces {
    +             em0 {
    +                 description "OOOB MANAGEMENT INTERFACE --- DO NOT DELETE";
    +                 unit 0 {
    +                     family inet {
    +                         address 192.168.1.11/24;
    +                     }
    +                 }
    +             }
    +         }
    +         routing-options {
    +             static {
    +                 route 0.0.0.0/0 next-hop 192.168.1.237;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-MPLS {
    +         protocols {
    +             mpls {
    +                 log-updown {
    +                     syslog;
    +                     trap;
    +                     trap-path-down;
    +                     trap-path-up;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-RSVP {
    +         protocols {
    +             rsvp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <ge-*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface <em*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface lo0.0 {
    +                     aggregate;
    +                     reliable;
    +                     link-protection;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-LDP {
    +         protocols {
    +             ldp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface lo0.0;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-ISIS {
    +         protocols {
    +             isis {
    +                 reference-bandwidth 10g;
    +                 traffic-engineering {
    +                     family inet {
    +                         shortcuts;
    +                     }
    +                     family inet6 {
    +                         shortcuts;
    +                     }
    +                 }
    +                 interface lo0.0 {
    +                     passive;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <em-*> {
    +                     node-link-protection;
    +                 }
    +             }
    +         }
    +     }
    + }
    + apply-groups OUT-OF-BAND-MANAGEMENT;
    [edit system]
    -  host-name LAB-COR1_bootstrap;
    +  host-name LAB-COR1;
    +  syslog {
    +      user * {
    +          any emergency;
    +      }
    +      file messages {
    +          any notice;
    +          authorization info;
    +      }
    +      file interactive-commands {
    +          interactive-commands any;
    +      }
    +  }
    +  ntp {
    +      boot-server 192.168.1.237;
    +      server 192.168.1.237;
    +  }
    [edit interfaces]
    +   /* link_index: 28 | LAB-COR1 em0.0 169.254.0.28/31 --> 169.254.0.29/31 em0.0 LAB-COR4 */
        em0 { ... }
    [edit interfaces em0]
    -   description "MANAGEMENT INTERFACE --- DO NOT DELETE";
    +   description "WAN | LAB-COR4 em0";
    +   mtu 2000;
    [edit interfaces em0 unit 0 family inet]
    +       address 169.254.0.28/31;
    -       address 192.168.1.11/24;
    [edit interfaces em0 unit 0]
    +      family iso;
    +      family mpls;
    [edit interfaces]
    +   /* link_index: 0 | LAB-COR1 em1.0 169.254.0.1/31 --> 169.254.0.0/31 em1.0 LAB-PE1 */
    +   em1 {
    +       description "WAN | LAB-PE1 em1";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.1/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 4 | LAB-COR1 em2.0 169.254.0.5/31 --> 169.254.0.4/31 em1.0 LAB-PE2 */
    +   em2 {
    +       description "WAN | LAB-PE2 em1";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.5/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 16 | LAB-COR1 em3.0 169.254.0.16/31 --> 169.254.0.17/31 em3.0 LAB-COR2 */
    +   em3 {
    +       description "WAN | LAB-COR2 em3";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.16/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 20 | LAB-COR1 em4.0 169.254.0.20/31 --> 169.254.0.21/31 em1.0 LAB-COR3 */
    +   em4 {
    +       description "WAN | LAB-COR3 em1";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.20/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 18 | LAB-COR1 em5.0 169.254.0.18/31 --> 169.254.0.19/31 em5.0 LAB-COR4 */
    +   em5 {
    +       description "WAN | LAB-COR4 em5";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.18/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   lo0 {
    +       unit 0 {
    +           description "PEERING INTERFACE --- DO NOT DELETE";
    +           family inet {
    +               address 10.1.1.11/32;
    +           }
    +           family iso {
    +               address 49.0000.0172.0016.0011.00;
    +           }
    +       }
    +   }
    [edit routing-options]
    -   static {
    -       route 0.0.0.0/0 next-hop 192.168.1.237;
    -   }
    +   router-id 10.1.1.11;
    +   autonomous-system 0.65535;
    +   forwarding-table {
    +       /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +       export load-balancing-policy;
    +   }
    +   dynamic-tunnels {
    +       dt-1 {
    +           rsvp-te rsvp-te-1 {
    +               label-switched-path-template {
    +                   default-template;
    +               }
    +               destination-networks {
    +                   10.1.1.0/24;
    +               }
    +           }
    +       }
    +   }
    [edit]
    +  protocols {
    +      rsvp {
    +          apply-groups PROTOCOL-DEFAULTS-RSVP;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em3.0;
    +          interface em5.0;
    +          interface em4.0;
    +          interface em0.0;
    +      }
    +      mpls {
    +          apply-groups PROTOCOL-DEFAULTS-MPLS;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em3.0;
    +          interface em5.0;
    +          interface em4.0;
    +          interface em0.0;
    +      }
    +      isis {
    +          apply-groups PROTOCOL-DEFAULTS-ISIS;
    +          interface em0.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em1.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em2.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em3.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em4.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em5.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +      }
    +      ldp {
    +          apply-groups PROTOCOL-DEFAULTS-LDP;
    +          keepalive-timeout 180;
    +          interface em0.0;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em3.0;
    +          interface em4.0;
    +          interface em5.0;
    +      }
    +      lldp {
    +          interface all;
    +      }
    +  }
    +  /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +  policy-options {
    +      policy-statement load-balancing-policy {
    +          then {
    +              load-balance per-packet;
    +          }
    +      }
    +  }
  * LAB-COR3                   - yellowchanged=True ----------------------------------------------------
    yellow[edit]
    + groups {
    +     OUT-OF-BAND-MANAGEMENT {
    +         interfaces {
    +             em0 {
    +                 description "OOOB MANAGEMENT INTERFACE --- DO NOT DELETE";
    +                 unit 0 {
    +                     family inet {
    +                         address 192.168.1.13/24;
    +                     }
    +                 }
    +             }
    +         }
    +         routing-options {
    +             static {
    +                 route 0.0.0.0/0 next-hop 192.168.1.237;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-MPLS {
    +         protocols {
    +             mpls {
    +                 log-updown {
    +                     syslog;
    +                     trap;
    +                     trap-path-down;
    +                     trap-path-up;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-RSVP {
    +         protocols {
    +             rsvp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <ge-*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface <em*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface lo0.0 {
    +                     aggregate;
    +                     reliable;
    +                     link-protection;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-LDP {
    +         protocols {
    +             ldp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface lo0.0;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-ISIS {
    +         protocols {
    +             isis {
    +                 reference-bandwidth 10g;
    +                 traffic-engineering {
    +                     family inet {
    +                         shortcuts;
    +                     }
    +                     family inet6 {
    +                         shortcuts;
    +                     }
    +                 }
    +                 interface lo0.0 {
    +                     passive;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <em-*> {
    +                     node-link-protection;
    +                 }
    +             }
    +         }
    +     }
    + }
    + apply-groups OUT-OF-BAND-MANAGEMENT;
    [edit system]
    -  host-name LAB-COR3_bootstrap;
    +  host-name LAB-COR3;
    +  syslog {
    +      user * {
    +          any emergency;
    +      }
    +      file messages {
    +          any notice;
    +          authorization info;
    +      }
    +      file interactive-commands {
    +          interactive-commands any;
    +      }
    +  }
    +  ntp {
    +      boot-server 192.168.1.237;
    +      server 192.168.1.237;
    +  }
    [edit interfaces]
    -   em0 {
    -       description "MANAGEMENT INTERFACE --- DO NOT DELETE";
    -       unit 0 {
    -           family inet {
    -               address 192.168.1.13/24;
    -           }
    -       }
    -   }
    +   /* link_index: 20 | LAB-COR3 em1.0 169.254.0.21/31 --> 169.254.0.20/31 em4.0 LAB-COR1 */
    +   em1 {
    +       description "WAN | LAB-COR1 em4";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.21/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 26 | LAB-COR3 em2.0 169.254.0.26/31 --> 169.254.0.27/31 em2.0 LAB-COR4 */
    +   em2 {
    +       description "WAN | LAB-COR4 em2";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.26/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 8 | LAB-COR3 em3.0 169.254.0.9/31 --> 169.254.0.8/31 em1.0 LAB-PE3 */
    +   em3 {
    +       description "WAN | LAB-PE3 em1";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.9/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 14 | LAB-COR3 em4.0 169.254.0.15/31 --> 169.254.0.14/31 em2.0 LAB-PE4 */
    +   em4 {
    +       description "WAN | LAB-PE4 em2";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.15/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 22 | LAB-COR3 em5.0 169.254.0.23/31 --> 169.254.0.22/31 em5.0 LAB-COR2 */
    +   em5 {
    +       description "WAN | LAB-COR2 em5";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.23/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   lo0 {
    +       unit 0 {
    +           description "PEERING INTERFACE --- DO NOT DELETE";
    +           family inet {
    +               address 10.1.1.13/32;
    +           }
    +           family iso {
    +               address 49.0000.0172.0016.0013.00;
    +           }
    +       }
    +   }
    [edit routing-options]
    -   static {
    -       route 0.0.0.0/0 next-hop 192.168.1.237;
    -   }
    +   router-id 10.1.1.13;
    +   autonomous-system 0.65535;
    +   forwarding-table {
    +       /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +       export load-balancing-policy;
    +   }
    +   dynamic-tunnels {
    +       dt-1 {
    +           rsvp-te rsvp-te-1 {
    +               label-switched-path-template {
    +                   default-template;
    +               }
    +               destination-networks {
    +                   10.1.1.0/24;
    +               }
    +           }
    +       }
    +   }
    [edit]
    +  protocols {
    +      rsvp {
    +          apply-groups PROTOCOL-DEFAULTS-RSVP;
    +          interface em3.0;
    +          interface em4.0;
    +          interface em1.0;
    +          interface em5.0;
    +          interface em2.0;
    +      }
    +      mpls {
    +          apply-groups PROTOCOL-DEFAULTS-MPLS;
    +          interface em3.0;
    +          interface em4.0;
    +          interface em1.0;
    +          interface em5.0;
    +          interface em2.0;
    +      }
    +      isis {
    +          apply-groups PROTOCOL-DEFAULTS-ISIS;
    +          interface em1.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em2.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em3.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em4.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em5.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +      }
    +      ldp {
    +          apply-groups PROTOCOL-DEFAULTS-LDP;
    +          keepalive-timeout 180;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em3.0;
    +          interface em4.0;
    +          interface em5.0;
    +      }
    +      lldp {
    +          interface all;
    +      }
    +  }
    +  /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +  policy-options {
    +      policy-statement load-balancing-policy {
    +          then {
    +              load-balance per-packet;
    +          }
    +      }
    +  }
  * LAB-COR2                   - yellowchanged=True ----------------------------------------------------
    yellow[edit]
    + groups {
    +     OUT-OF-BAND-MANAGEMENT {
    +         interfaces {
    +             em0 {
    +                 description "OOOB MANAGEMENT INTERFACE --- DO NOT DELETE";
    +                 unit 0 {
    +                     family inet {
    +                         address 192.168.1.12/24;
    +                     }
    +                 }
    +             }
    +         }
    +         routing-options {
    +             static {
    +                 route 0.0.0.0/0 next-hop 192.168.1.237;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-MPLS {
    +         protocols {
    +             mpls {
    +                 log-updown {
    +                     syslog;
    +                     trap;
    +                     trap-path-down;
    +                     trap-path-up;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-RSVP {
    +         protocols {
    +             rsvp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <ge-*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface <em*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface lo0.0 {
    +                     aggregate;
    +                     reliable;
    +                     link-protection;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-LDP {
    +         protocols {
    +             ldp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface lo0.0;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-ISIS {
    +         protocols {
    +             isis {
    +                 reference-bandwidth 10g;
    +                 traffic-engineering {
    +                     family inet {
    +                         shortcuts;
    +                     }
    +                     family inet6 {
    +                         shortcuts;
    +                     }
    +                 }
    +                 interface lo0.0 {
    +                     passive;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <em-*> {
    +                     node-link-protection;
    +                 }
    +             }
    +         }
    +     }
    + }
    + apply-groups OUT-OF-BAND-MANAGEMENT;
    [edit system]
    -  host-name LAB-COR2_bootstrap;
    +  host-name LAB-COR2;
    +  syslog {
    +      user * {
    +          any emergency;
    +      }
    +      file messages {
    +          any notice;
    +          authorization info;
    +      }
    +      file interactive-commands {
    +          interactive-commands any;
    +      }
    +  }
    +  ntp {
    +      boot-server 192.168.1.237;
    +      server 192.168.1.237;
    +  }
    [edit interfaces]
    -   em0 {
    -       description "MANAGEMENT INTERFACE --- DO NOT DELETE";
    -       unit 0 {
    -           family inet {
    -               address 192.168.1.12/24;
    -           }
    -       }
    -   }
    +   /* link_index: 2 | LAB-COR2 em1.0 169.254.0.3/31 --> 169.254.0.2/31 em2.0 LAB-PE1 */
    +   em1 {
    +       description "WAN | LAB-PE1 em2";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.3/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 6 | LAB-COR2 em2.0 169.254.0.7/31 --> 169.254.0.6/31 em2.0 LAB-PE2 */
    +   em2 {
    +       description "WAN | LAB-PE2 em2";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.7/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 16 | LAB-COR2 em3.0 169.254.0.17/31 --> 169.254.0.16/31 em3.0 LAB-COR1 */
    +   em3 {
    +       description "WAN | LAB-COR1 em3";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.17/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 24 | LAB-COR2 em4.0 169.254.0.24/31 --> 169.254.0.25/31 em1.0 LAB-COR4 */
    +   em4 {
    +       description "WAN | LAB-COR4 em1";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.24/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 22 | LAB-COR2 em5.0 169.254.0.22/31 --> 169.254.0.23/31 em5.0 LAB-COR3 */
    +   em5 {
    +       description "WAN | LAB-COR3 em5";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.22/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   lo0 {
    +       unit 0 {
    +           description "PEERING INTERFACE --- DO NOT DELETE";
    +           family inet {
    +               address 10.1.1.12/32;
    +           }
    +           family iso {
    +               address 49.0000.0172.0016.0012.00;
    +           }
    +       }
    +   }
    [edit routing-options]
    -   static {
    -       route 0.0.0.0/0 next-hop 192.168.1.237;
    -   }
    +   router-id 10.1.1.12;
    +   autonomous-system 0.65535;
    +   forwarding-table {
    +       /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +       export load-balancing-policy;
    +   }
    +   dynamic-tunnels {
    +       dt-1 {
    +           rsvp-te rsvp-te-1 {
    +               label-switched-path-template {
    +                   default-template;
    +               }
    +               destination-networks {
    +                   10.1.1.0/24;
    +               }
    +           }
    +       }
    +   }
    [edit]
    +  protocols {
    +      rsvp {
    +          apply-groups PROTOCOL-DEFAULTS-RSVP;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em3.0;
    +          interface em5.0;
    +          interface em4.0;
    +      }
    +      mpls {
    +          apply-groups PROTOCOL-DEFAULTS-MPLS;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em3.0;
    +          interface em5.0;
    +          interface em4.0;
    +      }
    +      isis {
    +          apply-groups PROTOCOL-DEFAULTS-ISIS;
    +          interface em1.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em2.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em3.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em4.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em5.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +      }
    +      ldp {
    +          apply-groups PROTOCOL-DEFAULTS-LDP;
    +          keepalive-timeout 180;
    +          interface em1.0;
    +          interface em2.0;
    +          interface em3.0;
    +          interface em4.0;
    +          interface em5.0;
    +      }
    +      lldp {
    +          interface all;
    +      }
    +  }
    +  /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +  policy-options {
    +      policy-statement load-balancing-policy {
    +          then {
    +              load-balance per-packet;
    +          }
    +      }
    +  }
  * LAB-PE2                    - yellowchanged=True ----------------------------------------------------
    yellow[edit]
    + groups {
    +     OUT-OF-BAND-MANAGEMENT {
    +         interfaces {
    +             em0 {
    +                 description "OOOB MANAGEMENT INTERFACE --- DO NOT DELETE";
    +                 unit 0 {
    +                     family inet {
    +                         address 192.168.1.2/24;
    +                     }
    +                 }
    +             }
    +         }
    +         routing-options {
    +             static {
    +                 route 0.0.0.0/0 next-hop 192.168.1.237;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-MPLS {
    +         protocols {
    +             mpls {
    +                 log-updown {
    +                     syslog;
    +                     trap;
    +                     trap-path-down;
    +                     trap-path-up;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-RSVP {
    +         protocols {
    +             rsvp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <ge-*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface <em*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface lo0.0 {
    +                     aggregate;
    +                     reliable;
    +                     link-protection;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-LDP {
    +         protocols {
    +             ldp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface lo0.0;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-ISIS {
    +         protocols {
    +             isis {
    +                 reference-bandwidth 10g;
    +                 traffic-engineering {
    +                     family inet {
    +                         shortcuts;
    +                     }
    +                     family inet6 {
    +                         shortcuts;
    +                     }
    +                 }
    +                 interface lo0.0 {
    +                     passive;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <em-*> {
    +                     node-link-protection;
    +                 }
    +             }
    +         }
    +     }
    + }
    + apply-groups OUT-OF-BAND-MANAGEMENT;
    [edit system]
    -  host-name LAB-PE2_bootstrap;
    +  host-name LAB-PE2;
    +  syslog {
    +      user * {
    +          any emergency;
    +      }
    +      file messages {
    +          any notice;
    +          authorization info;
    +      }
    +      file interactive-commands {
    +          interactive-commands any;
    +      }
    +  }
    +  ntp {
    +      boot-server 192.168.1.237;
    +      server 192.168.1.237;
    +  }
    [edit interfaces]
    -   em0 {
    -       description "MANAGEMENT INTERFACE --- DO NOT DELETE";
    -       unit 0 {
    -           family inet {
    -               address 192.168.1.2/24;
    -           }
    -       }
    -   }
    +   /* link_index: 4 | LAB-PE2 em1.0 169.254.0.4/31 --> 169.254.0.5/31 em2.0 LAB-COR1 */
    +   em1 {
    +       description "WAN | LAB-COR1 em2";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.4/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 6 | LAB-PE2 em2.0 169.254.0.6/31 --> 169.254.0.7/31 em2.0 LAB-COR2 */
    +   em2 {
    +       description "WAN | LAB-COR2 em2";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.6/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   lo0 {
    +       unit 0 {
    +           description "PEERING INTERFACE --- DO NOT DELETE";
    +           family inet {
    +               address 10.1.1.2/32;
    +           }
    +           family iso {
    +               address 49.0000.0172.0016.0002.00;
    +           }
    +       }
    +   }
    [edit routing-options]
    -   static {
    -       route 0.0.0.0/0 next-hop 192.168.1.237;
    -   }
    +   router-id 10.1.1.2;
    +   autonomous-system 0.65535;
    +   forwarding-table {
    +       /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +       export load-balancing-policy;
    +   }
    +   dynamic-tunnels {
    +       dt-1 {
    +           rsvp-te rsvp-te-1 {
    +               label-switched-path-template {
    +                   default-template;
    +               }
    +               destination-networks {
    +                   10.1.1.0/24;
    +               }
    +           }
    +       }
    +   }
    [edit]
    +  protocols {
    +      rsvp {
    +          apply-groups PROTOCOL-DEFAULTS-RSVP;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      mpls {
    +          apply-groups PROTOCOL-DEFAULTS-MPLS;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      isis {
    +          apply-groups PROTOCOL-DEFAULTS-ISIS;
    +          interface em1.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em2.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +      }
    +      ldp {
    +          apply-groups PROTOCOL-DEFAULTS-LDP;
    +          keepalive-timeout 180;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      lldp {
    +          interface all;
    +      }
    +  }
    +  /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +  policy-options {
    +      policy-statement load-balancing-policy {
    +          then {
    +              load-balance per-packet;
    +          }
    +      }
    +  }
  * LAB-PE3                    - yellowchanged=True ----------------------------------------------------
    yellow[edit]
    + groups {
    +     OUT-OF-BAND-MANAGEMENT {
    +         interfaces {
    +             em0 {
    +                 description "OOOB MANAGEMENT INTERFACE --- DO NOT DELETE";
    +                 unit 0 {
    +                     family inet {
    +                         address 192.168.1.3/24;
    +                     }
    +                 }
    +             }
    +         }
    +         routing-options {
    +             static {
    +                 route 0.0.0.0/0 next-hop 192.168.1.237;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-MPLS {
    +         protocols {
    +             mpls {
    +                 log-updown {
    +                     syslog;
    +                     trap;
    +                     trap-path-down;
    +                     trap-path-up;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-RSVP {
    +         protocols {
    +             rsvp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <ge-*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface <em*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface lo0.0 {
    +                     aggregate;
    +                     reliable;
    +                     link-protection;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-LDP {
    +         protocols {
    +             ldp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface lo0.0;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-ISIS {
    +         protocols {
    +             isis {
    +                 reference-bandwidth 10g;
    +                 traffic-engineering {
    +                     family inet {
    +                         shortcuts;
    +                     }
    +                     family inet6 {
    +                         shortcuts;
    +                     }
    +                 }
    +                 interface lo0.0 {
    +                     passive;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <em-*> {
    +                     node-link-protection;
    +                 }
    +             }
    +         }
    +     }
    + }
    + apply-groups OUT-OF-BAND-MANAGEMENT;
    [edit system]
    -  host-name LAB-PE3_bootstrap;
    +  host-name LAB-PE3;
    +  syslog {
    +      user * {
    +          any emergency;
    +      }
    +      file messages {
    +          any notice;
    +          authorization info;
    +      }
    +      file interactive-commands {
    +          interactive-commands any;
    +      }
    +  }
    +  ntp {
    +      boot-server 192.168.1.237;
    +      server 192.168.1.237;
    +  }
    [edit interfaces]
    -   em0 {
    -       description "MANAGEMENT INTERFACE --- DO NOT DELETE";
    -       unit 0 {
    -           family inet {
    -               address 192.168.1.3/24;
    -           }
    -       }
    -   }
    +   /* link_index: 8 | LAB-PE3 em1.0 169.254.0.8/31 --> 169.254.0.9/31 em3.0 LAB-COR3 */
    +   em1 {
    +       description "WAN | LAB-COR3 em3";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.8/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 10 | LAB-PE3 em2.0 169.254.0.10/31 --> 169.254.0.11/31 em4.0 LAB-COR4 */
    +   em2 {
    +       description "WAN | LAB-COR4 em4";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.10/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   lo0 {
    +       unit 0 {
    +           description "PEERING INTERFACE --- DO NOT DELETE";
    +           family inet {
    +               address 10.1.1.3/32;
    +           }
    +           family iso {
    +               address 49.0000.0172.0016.0003.00;
    +           }
    +       }
    +   }
    [edit routing-options]
    -   static {
    -       route 0.0.0.0/0 next-hop 192.168.1.237;
    -   }
    +   router-id 10.1.1.3;
    +   autonomous-system 0.65535;
    +   forwarding-table {
    +       /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +       export load-balancing-policy;
    +   }
    +   dynamic-tunnels {
    +       dt-1 {
    +           rsvp-te rsvp-te-1 {
    +               label-switched-path-template {
    +                   default-template;
    +               }
    +               destination-networks {
    +                   10.1.1.0/24;
    +               }
    +           }
    +       }
    +   }
    [edit]
    +  protocols {
    +      rsvp {
    +          apply-groups PROTOCOL-DEFAULTS-RSVP;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      mpls {
    +          apply-groups PROTOCOL-DEFAULTS-MPLS;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      isis {
    +          apply-groups PROTOCOL-DEFAULTS-ISIS;
    +          interface em1.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em2.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +      }
    +      ldp {
    +          apply-groups PROTOCOL-DEFAULTS-LDP;
    +          keepalive-timeout 180;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      lldp {
    +          interface all;
    +      }
    +  }
    +  /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +  policy-options {
    +      policy-statement load-balancing-policy {
    +          then {
    +              load-balance per-packet;
    +          }
    +      }
    +  }
  * LAB-PE4                    - yellowchanged=True ----------------------------------------------------
    yellow[edit]
    + groups {
    +     OUT-OF-BAND-MANAGEMENT {
    +         interfaces {
    +             em0 {
    +                 description "OOOB MANAGEMENT INTERFACE --- DO NOT DELETE";
    +                 unit 0 {
    +                     family inet {
    +                         address 192.168.1.4/24;
    +                     }
    +                 }
    +             }
    +         }
    +         routing-options {
    +             static {
    +                 route 0.0.0.0/0 next-hop 192.168.1.237;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-MPLS {
    +         protocols {
    +             mpls {
    +                 log-updown {
    +                     syslog;
    +                     trap;
    +                     trap-path-down;
    +                     trap-path-up;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-RSVP {
    +         protocols {
    +             rsvp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <ge-*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface <em*> {
    +                     aggregate;
    +                     reliable;
    +                     subscription 60;
    +                     link-protection;
    +                 }
    +                 interface lo0.0 {
    +                     aggregate;
    +                     reliable;
    +                     link-protection;
    +                 }
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-LDP {
    +         protocols {
    +             ldp {
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface lo0.0;
    +             }
    +         }
    +     }
    +     PROTOCOL-DEFAULTS-ISIS {
    +         protocols {
    +             isis {
    +                 reference-bandwidth 10g;
    +                 traffic-engineering {
    +                     family inet {
    +                         shortcuts;
    +                     }
    +                     family inet6 {
    +                         shortcuts;
    +                     }
    +                 }
    +                 interface lo0.0 {
    +                     passive;
    +                 }
    +                 interface fxp0.0 {
    +                     disable;
    +                 }
    +                 interface em0.0 {
    +                     disable;
    +                 }
    +                 interface <em-*> {
    +                     node-link-protection;
    +                 }
    +             }
    +         }
    +     }
    + }
    + apply-groups OUT-OF-BAND-MANAGEMENT;
    [edit system]
    -  host-name LAB-PE4_bootstrap;
    +  host-name LAB-PE4;
    +  syslog {
    +      user * {
    +          any emergency;
    +      }
    +      file messages {
    +          any notice;
    +          authorization info;
    +      }
    +      file interactive-commands {
    +          interactive-commands any;
    +      }
    +  }
    +  ntp {
    +      boot-server 192.168.1.237;
    +      server 192.168.1.237;
    +  }
    [edit interfaces]
    -   em0 {
    -       description "MANAGEMENT INTERFACE --- DO NOT DELETE";
    -       unit 0 {
    -           family inet {
    -               address 192.168.1.4/24;
    -           }
    -       }
    -   }
    +   /* link_index: 12 | LAB-PE4 em1.0 169.254.0.12/31 --> 169.254.0.13/31 em3.0 LAB-COR4 */
    +   em1 {
    +       description "WAN | LAB-COR4 em3";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.12/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   /* link_index: 14 | LAB-PE4 em2.0 169.254.0.14/31 --> 169.254.0.15/31 em4.0 LAB-COR3 */
    +   em2 {
    +       description "WAN | LAB-COR3 em4";
    +       mtu 2000;
    +       unit 0 {
    +           family inet {
    +               address 169.254.0.14/31;
    +           }
    +           family iso;
    +           family mpls;
    +       }
    +   }
    +   lo0 {
    +       unit 0 {
    +           description "PEERING INTERFACE --- DO NOT DELETE";
    +           family inet {
    +               address 10.1.1.4/32;
    +           }
    +           family iso {
    +               address 49.0000.0172.0016.0004.00;
    +           }
    +       }
    +   }
    [edit routing-options]
    -   static {
    -       route 0.0.0.0/0 next-hop 192.168.1.237;
    -   }
    +   router-id 10.1.1.4;
    +   autonomous-system 0.65535;
    +   forwarding-table {
    +       /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +       export load-balancing-policy;
    +   }
    +   dynamic-tunnels {
    +       dt-1 {
    +           rsvp-te rsvp-te-1 {
    +               label-switched-path-template {
    +                   default-template;
    +               }
    +               destination-networks {
    +                   10.1.1.0/24;
    +               }
    +           }
    +       }
    +   }
    [edit]
    +  protocols {
    +      rsvp {
    +          apply-groups PROTOCOL-DEFAULTS-RSVP;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      mpls {
    +          apply-groups PROTOCOL-DEFAULTS-MPLS;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      isis {
    +          apply-groups PROTOCOL-DEFAULTS-ISIS;
    +          interface em1.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +          interface em2.0 {
    +              point-to-point;
    +              level 1 disable;
    +              level 2 {
    +                  metric 10;
    +                  hello-interval 60;
    +              }
    +          }
    +      }
    +      ldp {
    +          apply-groups PROTOCOL-DEFAULTS-LDP;
    +          keepalive-timeout 180;
    +          interface em1.0;
    +          interface em2.0;
    +      }
    +      lldp {
    +          interface all;
    +      }
    +  }
    +  /* Best Practice: You must configure per-packet load-balancing routing policy when using ospf/isis node-link-protection */
    +  policy-options {
    +      policy-statement load-balancing-policy {
    +          then {
    +              load-balance per-packet;
    +          }
    +      }
    +  }

# STATS *******************************************************************************************************************
yellowLAB-COR1    : ok=13       changed=3       failed=0        unreachable=0
yellowLAB-COR2    : ok=10       changed=3       failed=0        unreachable=0
yellowLAB-COR3    : ok=10       changed=3       failed=0        unreachable=0
yellowLAB-COR4    : ok=10       changed=3       failed=0        unreachable=0
yellowLAB-PE1    : ok=10        changed=3       failed=0        unreachable=0
yellowLAB-PE2    : ok=10        changed=3       failed=0        unreachable=0
yellowLAB-PE3    : ok=10        changed=3       failed=0        unreachable=0
yellowLAB-PE4    : ok=10        changed=3       failed=0        unreachable=0


----- Configurations and diffs can be found in compiled/ directory -----
----- Generated Diff files -----
compiled/LAB-COR1/show-compare.diff
compiled/LAB-COR2/show-compare.diff
compiled/LAB-COR3/show-compare.diff
compiled/LAB-COR4/show-compare.diff
compiled/LAB-PE1/show-compare.diff
compiled/LAB-PE2/show-compare.diff
compiled/LAB-PE3/show-compare.diff
compiled/LAB-PE4/show-compare.diff

----- End of script -----
```