
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMBIENT BASENAME BOX CAMERA CO COMMENT CONE CONSTANTS CYLINDER DISPLAY DOUBLE FOCAL FRAMES GENERATE_RAYFILES ID INT LIGHT LINE MESH MOVE POP PUSH ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SPHERE STRING TEXTURE TORUS TWEEN VARY WEB XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEcommand : POP\n                 | PUSHcommand : SCREEN NUMBER NUMBER\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : CONE NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONE NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES NUMBERcommand : BASENAME TEXTcommand : VARY SYMBOL NUMBER NUMBER NUMBER NUMBERcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT NUMBER NUMBER NUMBERcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'BOX':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[1,-60,-14,-3,-9,-10,-69,-12,1,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'GENERATE_RAYFILES':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[2,-60,-14,-3,-9,-10,-69,-12,2,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'CYLINDER':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[3,-60,-14,-3,-9,-10,-69,-12,3,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'SCALE':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[4,-60,-14,-3,-9,-10,-69,-12,4,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'LIGHT':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[18,-60,-14,-3,-9,-10,-69,-12,18,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'BASENAME':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[13,-60,-14,-3,-9,-10,-69,-12,13,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'MOVE':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[5,-60,-14,-3,-9,-10,-69,-12,5,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'VARY':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[6,-60,-14,-3,-9,-10,-69,-12,6,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'TEXTURE':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[7,-60,-14,-3,-9,-10,-69,-12,7,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'SAVE_COORDS':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[8,-60,-14,-3,-9,-10,-69,-12,8,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'CONE':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[9,-60,-14,-3,-9,-10,-69,-12,9,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'FRAMES':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[10,-60,-14,-3,-9,-10,-69,-12,10,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'LINE':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[11,-60,-14,-3,-9,-10,-69,-12,11,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'DISPLAY':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[12,-60,-14,-3,-9,-10,-69,-12,12,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'COMMENT':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[14,-60,-14,-3,-9,-10,-69,-12,14,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'SET':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[15,-60,-14,-3,-9,-10,-69,-12,15,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'POP':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[16,-60,-14,-3,-9,-10,-69,-12,16,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'SHADING_TYPE':([29,],[69,]),'CAMERA':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[17,-60,-14,-3,-9,-10,-69,-12,17,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'PUSH':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[19,-60,-14,-3,-9,-10,-69,-12,19,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'SHADING':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[29,-60,-14,-3,-9,-10,-69,-12,29,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'SCREEN':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[24,-60,-14,-3,-9,-10,-69,-12,24,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'FOCAL':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[22,-60,-14,-3,-9,-10,-69,-12,22,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'$end':([0,2,12,14,16,19,20,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,72,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[-1,-60,-14,-3,-9,-10,0,-69,-12,-1,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-2,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'WEB':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[23,-60,-14,-3,-9,-10,-69,-12,23,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'CO':([28,39,40,68,],[67,-5,-4,98,]),'STRING':([13,34,39,40,53,55,67,74,98,],[53,53,-5,-4,-7,-6,53,53,53,]),'TORUS':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[21,-60,-14,-3,-9,-10,-69,-12,21,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'ROTATE':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[30,-60,-14,-3,-9,-10,-69,-12,30,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'TWEEN':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[26,-60,-14,-3,-9,-10,-69,-12,26,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'SPHERE':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[27,-60,-14,-3,-9,-10,-69,-12,27,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'MESH':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[28,-60,-14,-3,-9,-10,-69,-12,28,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'ID':([1,3,6,7,8,9,11,13,15,18,21,25,27,28,34,35,36,39,40,53,55,67,74,94,97,98,99,107,108,113,119,123,139,146,151,156,163,165,169,171,173,175,182,185,191,193,200,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-8,-5,-4,-7,-6,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'SAVE_KNOBS':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[25,-60,-14,-3,-9,-10,-69,-12,25,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'DOUBLE':([1,3,4,5,9,10,11,17,21,22,24,26,27,31,33,36,37,38,39,40,41,42,43,44,45,46,48,49,51,52,56,57,58,59,60,62,64,65,66,70,73,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,92,95,96,100,102,103,104,105,106,109,110,111,112,113,114,115,116,117,118,120,121,126,127,128,129,130,133,134,135,136,137,138,139,140,141,142,143,145,148,149,150,152,154,155,157,158,159,160,161,162,164,167,168,172,176,177,178,180,184,188,192,196,198,202,203,205,206,207,208,209,210,211,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-8,36,36,-5,-4,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'XYZ':([1,3,6,7,8,9,11,13,15,18,21,25,27,28,30,34,35,36,39,40,53,55,67,74,94,97,98,99,107,108,113,119,123,139,146,151,156,163,165,169,171,173,175,182,185,191,193,200,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,70,40,40,-8,-5,-4,-7,-6,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'SET_KNOBS':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[31,-60,-14,-3,-9,-10,-69,-12,31,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'AMBIENT':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[33,-60,-14,-3,-9,-10,-69,-12,33,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'SAVE':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[34,-60,-14,-3,-9,-10,-69,-12,34,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),'CONSTANTS':([0,2,12,14,16,19,23,24,32,36,39,40,47,50,53,54,55,61,63,69,71,88,93,97,99,101,107,108,122,123,124,125,131,132,144,146,147,151,153,156,163,165,166,169,170,171,173,174,175,179,181,182,183,185,186,187,189,190,191,193,194,195,197,199,200,201,204,207,212,213,],[35,-60,-14,-3,-9,-10,-69,-12,35,-8,-5,-4,-66,-49,-7,-50,-6,-68,-65,-58,-53,-52,-11,-61,-48,-13,-46,-44,-63,-62,-47,-54,-45,-43,-67,-15,-64,-27,-51,-31,-19,-16,-17,-23,-28,-29,-33,-32,-35,-59,-20,-21,-18,-25,-24,-30,-34,-36,-37,-39,-57,-22,-26,-38,-41,-40,-42,-55,-70,-56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,32,],[20,72,]),'SYMBOL':([1,3,6,7,8,9,11,13,15,18,21,25,27,28,34,35,67,74,94,97,98,99,107,108,113,119,123,139,146,151,156,163,165,169,171,173,175,182,185,191,193,200,],[37,42,45,46,47,48,52,55,56,58,60,63,65,68,55,75,55,55,119,122,55,124,131,132,138,144,147,159,166,170,174,181,183,186,187,189,190,195,197,199,201,204,]),'command':([0,32,],[32,32,]),'NUMBER':([1,3,4,5,9,10,11,17,21,22,24,26,27,31,33,37,38,41,42,43,44,45,46,48,49,51,52,56,57,58,59,60,62,64,65,66,70,73,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,92,95,96,100,102,103,104,105,106,109,110,111,112,113,114,115,116,117,118,120,121,126,127,128,129,130,133,134,135,136,137,138,139,140,141,142,143,145,148,149,150,152,154,155,157,158,159,160,161,162,164,167,168,172,176,177,178,180,184,188,192,196,198,202,203,205,206,207,208,209,210,211,],[38,41,43,44,49,50,51,57,59,61,62,64,66,71,73,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,100,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,125,126,127,128,129,130,133,134,135,136,137,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,160,161,162,163,164,165,167,168,169,171,172,173,175,176,177,178,179,180,182,184,185,188,191,192,193,194,196,198,200,202,203,205,206,207,208,209,210,211,212,213,]),'TEXT':([13,34,67,74,98,],[54,74,97,101,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> <empty>','input',0,'p_input','mdl.py',126),
  ('input -> command input','input',2,'p_input','mdl.py',127),
  ('command -> COMMENT','command',1,'p_command_comment','mdl.py',131),
  ('SYMBOL -> XYZ','SYMBOL',1,'p_SYMBOL','mdl.py',135),
  ('SYMBOL -> ID','SYMBOL',1,'p_SYMBOL','mdl.py',136),
  ('TEXT -> SYMBOL','TEXT',1,'p_TEXT','mdl.py',140),
  ('TEXT -> STRING','TEXT',1,'p_TEXT','mdl.py',141),
  ('NUMBER -> DOUBLE','NUMBER',1,'p_NUMBER','mdl.py',145),
  ('command -> POP','command',1,'p_command_stack','mdl.py',149),
  ('command -> PUSH','command',1,'p_command_stack','mdl.py',150),
  ('command -> SCREEN NUMBER NUMBER','command',3,'p_command_screen','mdl.py',154),
  ('command -> SCREEN','command',1,'p_command_screen','mdl.py',155),
  ('command -> SAVE TEXT TEXT','command',3,'p_command_save','mdl.py',162),
  ('command -> DISPLAY','command',1,'p_command_show','mdl.py',166),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER','command',5,'p_command_sphere','mdl.py',170),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_sphere','mdl.py',171),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL','command',6,'p_command_sphere','mdl.py',172),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_sphere','mdl.py',173),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_torus','mdl.py',187),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_torus','mdl.py',188),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_torus','mdl.py',189),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_torus','mdl.py',190),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_box','mdl.py',204),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_box','mdl.py',205),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_box','mdl.py',206),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_box','mdl.py',207),
  ('command -> CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_cylinder','mdl.py',222),
  ('command -> CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_cylinder','mdl.py',223),
  ('command -> CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_cylinder','mdl.py',224),
  ('command -> CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_cylinder','mdl.py',225),
  ('command -> CONE NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_cone','mdl.py',239),
  ('command -> CONE NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_cone','mdl.py',240),
  ('command -> CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_cone','mdl.py',241),
  ('command -> CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_cone','mdl.py',242),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',256),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',257),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',258),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',259),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',260),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',261),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',262),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',263),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',284),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',285),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',293),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',294),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',302),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',303),
  ('command -> FRAMES NUMBER','command',2,'p_command_frames','mdl.py',311),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',316),
  ('command -> VARY SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_vary','mdl.py',321),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',327),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',328),
  ('command -> AMBIENT NUMBER NUMBER NUMBER','command',4,'p_command_ambient','mdl.py',339),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',345),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',346),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_light','mdl.py',352),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',358),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',364),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',369),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',373),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',374),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',375),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',376),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',390),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',396),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',403),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',408),
  ('command -> WEB','command',1,'p_web','mdl.py',412),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',416),
]
