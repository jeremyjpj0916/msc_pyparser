
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATSIGN BACKSLASH COLON COMMA COMMENT CONFDIR_SECACTION CONFDIR_SECCOMPSIGNATURE CONFDIR_SECMARKER CONFDIR_SECRULE EQUALMARK EXCLAMMARK NUMBER PIPE QUOTED QUOTES SECCOMPSIGNARG SECMARKERARG SECRULE_ACTION SECRULE_ACTION_ARG SECRULE_ACTION_CTLACTION SECRULE_ACTION_CTLACTIONARG SECRULE_ACTION_CTLACTIONARGPARAM SECRULE_ACTION_INITCOLACTIONARG SECRULE_ACTION_INITCOLACTIONARGPARAM SECRULE_ACTION_SKIPAFTERACTIONARG SECRULE_ACTION_TRANSFORMS SECRULE_OPERATOR SECRULE_OPERATOR_ARG SECRULE_OPERATOR_ARG_NOQUOTE SECRULE_VARIABLE SECRULE_VARIABLE_ARG SEMICOLONmodsec_config : comment_line\n                        | secrule_line\n                        | seccompsignature_line\n                        | secaction_line\n                        | modsec_config secaction_line\n                        | secmarker_line\n                        | modsec_config secmarker_line\n                        | modsec_config seccompsignature_line\n                        | modsec_config comment_line\n                        | modsec_config secrule_linecomment_line : COMMENTseccompsignature_line : CONFDIR_SECCOMPSIGNATURE QUOTED SECCOMPSIGNARG QUOTEDsecaction_line : tok_confdir_secaction QUOTED secaction_expr_list QUOTEDtok_confdir_secaction : CONFDIR_SECACTIONsecmarker_line  : secmarker_line_quoted\n                            | secmarker_line_noquotedsecmarker_line_quoted  : CONFDIR_SECMARKER QUOTED SECMARKERARG QUOTEDsecmarker_line_noquoted  : CONFDIR_SECMARKER SECMARKERARGsecrule_line  : tok_confdir_secrule secvariable_expr_list QUOTED secoperator_expr QUOTED QUOTED secaction_expr_list QUOTED\n                        | tok_confdir_secrule secvariable_expr_list QUOTED secoperator_expr QUOTED\n                        | tok_confdir_secrule secvariable_expr_list secoperatorarg_noquote QUOTED secaction_expr_list QUOTED\n                        | tok_confdir_secrule secvariable_expr_list secoperatorarg_noquotetok_confdir_secrule : CONFDIR_SECRULEsecvariable_expr_list  : secvariable_expr\n                                | secvariable_expr_list PIPE secvariable_expr\n                                | secvariable_expr_list COMMA secvariable_exprsecvariable_expr  : tok_secrule_variable\n                            | tok_secrule_variable_prefix\n                            | tok_secrule_variable_with_arg\n                            | tok_secrule_variable_prefix_with_argtok_secrule_variable : SECRULE_VARIABLEtok_secrule_variable_prefix : secvariable_prefix tok_secrule_variabletok_secrule_variable_with_arg : tok_secrule_variable tok_secrule_variable_colon secvariable_argtok_secrule_variable_prefix_with_arg : secvariable_prefix tok_secrule_variable tok_secrule_variable_colon secvariable_argtok_secrule_variable_colon : COLONsecvariable_prefix : AND\n                              | EXCLAMMARK\n                              | EXCLAMMARK ANDsecvariable_arg  : tok_secrule_variable_arg\n                            | tok_secrule_variable_arg_quotestok_secrule_variable_arg : SECRULE_VARIABLE_ARGtok_secrule_variable_arg_quotes : QUOTES SECRULE_VARIABLE_ARG QUOTESsecoperator_expr  : tok_secoperator_group\n                             | tok_secoperator_group secoperator_arg_group\n                             | secoperator_arg_grouptok_secoperator_group : ATSIGN SECRULE_OPERATOR\n                                | EXCLAMMARK ATSIGN SECRULE_OPERATOR\n                                | EXCLAMMARKsecoperator_arg_group : SECRULE_OPERATOR_ARG\n                                | NUMBERsecoperatorarg_noquote : SECRULE_OPERATOR_ARG_NOQUOTEsecaction_expr_list  : secaction_expr\n                                | secaction_expr_list COMMA secaction_exprsecaction_expr       : tok_secrule_action\n                                | tok_secrule_action COLON secrule_action_argument\n                                | tok_secrule_action COLON QUOTES secrule_action_argument_singlequoted QUOTES\n                                | tok_secrule_action COLON secrule_action_argument EQUALMARK tok_secrule_action_ctlactionarg\n                                | tok_secrule_action COLON secrule_action_argument EQUALMARK tok_secrule_action_ctlactionarg SEMICOLON tok_secrule_action_ctlactionargparamtok_secrule_action : SECRULE_ACTIONsecrule_action_argument : SECRULE_ACTION_ARG\n                                | NUMBER\n                                | SECRULE_ACTION_TRANSFORMS\n                                | SECRULE_ACTION_CTLACTION\n                                | SECRULE_ACTION_SKIPAFTERACTIONARG\n                                | SECRULE_ACTION_INITCOLACTIONARGsecrule_action_argument_singlequoted : SECRULE_ACTION_ARG\n                                                | EXCLAMMARK SECRULE_ACTION_ARG\n                                                | NUMBERtok_secrule_action_ctlactionarg : SECRULE_ACTION_CTLACTIONARG\n                                        | SECRULE_ACTION_INITCOLACTIONARGPARAMtok_secrule_action_ctlactionargparam  : SECRULE_ACTION_CTLACTIONARGPARAM'
    
_lr_action_items = {'COMMENT':([0,1,2,3,4,5,6,7,11,12,16,17,18,19,20,34,36,39,66,67,70,71,89,102,],[7,7,-1,-2,-3,-4,-6,-11,-15,-16,-5,-7,-8,-9,-10,-18,-22,-51,-12,-13,-17,-20,-21,-19,]),'CONFDIR_SECCOMPSIGNATURE':([0,1,2,3,4,5,6,7,11,12,16,17,18,19,20,34,36,39,66,67,70,71,89,102,],[9,9,-1,-2,-3,-4,-6,-11,-15,-16,-5,-7,-8,-9,-10,-18,-22,-51,-12,-13,-17,-20,-21,-19,]),'CONFDIR_SECRULE':([0,1,2,3,4,5,6,7,11,12,16,17,18,19,20,34,36,39,66,67,70,71,89,102,],[13,13,-1,-2,-3,-4,-6,-11,-15,-16,-5,-7,-8,-9,-10,-18,-22,-51,-12,-13,-17,-20,-21,-19,]),'CONFDIR_SECACTION':([0,1,2,3,4,5,6,7,11,12,16,17,18,19,20,34,36,39,66,67,70,71,89,102,],[14,14,-1,-2,-3,-4,-6,-11,-15,-16,-5,-7,-8,-9,-10,-18,-22,-51,-12,-13,-17,-20,-21,-19,]),'CONFDIR_SECMARKER':([0,1,2,3,4,5,6,7,11,12,16,17,18,19,20,34,36,39,66,67,70,71,89,102,],[15,15,-1,-2,-3,-4,-6,-11,-15,-16,-5,-7,-8,-9,-10,-18,-22,-51,-12,-13,-17,-20,-21,-19,]),'$end':([1,2,3,4,5,6,7,11,12,16,17,18,19,20,34,36,39,66,67,70,71,89,102,],[0,-1,-2,-3,-4,-6,-11,-15,-16,-5,-7,-8,-9,-10,-18,-22,-51,-12,-13,-17,-20,-21,-19,]),'SECRULE_VARIABLE':([8,13,28,29,30,37,38,43,],[27,-23,27,-36,-37,27,27,-38,]),'AND':([8,13,30,37,38,],[29,-23,43,29,29,]),'EXCLAMMARK':([8,13,35,37,38,80,],[30,-23,54,30,30,94,]),'QUOTED':([9,10,14,15,21,22,23,24,25,26,27,36,39,42,44,45,46,47,48,49,50,51,52,54,55,56,58,59,60,61,62,63,71,72,73,75,77,78,79,81,82,83,84,85,86,88,90,96,97,98,99,100,104,105,],[31,32,-14,33,35,-24,-27,-28,-29,-30,-31,57,-51,-32,66,67,-52,-54,-59,70,71,-43,-45,-48,-49,-50,-25,-26,-33,-39,-40,-41,87,-44,-46,89,-34,-53,-55,-60,-61,-62,-63,-64,-65,-47,-42,102,-57,-69,-70,-56,-58,-71,]),'SECMARKERARG':([15,33,],[34,49,]),'PIPE':([21,22,23,24,25,26,27,42,58,59,60,61,62,63,77,90,],[37,-24,-27,-28,-29,-30,-31,-32,-25,-26,-33,-39,-40,-41,-34,-42,]),'COMMA':([21,22,23,24,25,26,27,42,45,46,47,48,58,59,60,61,62,63,75,77,78,79,81,82,83,84,85,86,90,96,97,98,99,100,104,105,],[38,-24,-27,-28,-29,-30,-31,-32,68,-52,-54,-59,-25,-26,-33,-39,-40,-41,68,-34,-53,-55,-60,-61,-62,-63,-64,-65,-42,68,-57,-69,-70,-56,-58,-71,]),'SECRULE_OPERATOR_ARG_NOQUOTE':([21,22,23,24,25,26,27,42,58,59,60,61,62,63,77,90,],[39,-24,-27,-28,-29,-30,-31,-32,-25,-26,-33,-39,-40,-41,-34,-42,]),'COLON':([23,27,42,47,48,],[41,-31,41,69,-59,]),'SECCOMPSIGNARG':([31,],[44,]),'SECRULE_ACTION':([32,57,68,87,],[48,48,48,48,]),'ATSIGN':([35,54,],[53,74,]),'SECRULE_OPERATOR_ARG':([35,51,54,73,88,],[55,55,-48,-46,-47,]),'NUMBER':([35,51,54,69,73,80,88,],[56,56,-48,82,-46,95,-47,]),'SECRULE_VARIABLE_ARG':([40,41,64,65,],[63,-35,76,63,]),'QUOTES':([40,41,65,69,76,92,93,95,101,],[64,-35,64,80,90,100,-66,-68,-67,]),'SECRULE_OPERATOR':([53,74,],[73,88,]),'SECRULE_ACTION_ARG':([69,80,94,],[81,93,101,]),'SECRULE_ACTION_TRANSFORMS':([69,],[83,]),'SECRULE_ACTION_CTLACTION':([69,],[84,]),'SECRULE_ACTION_SKIPAFTERACTIONARG':([69,],[85,]),'SECRULE_ACTION_INITCOLACTIONARG':([69,],[86,]),'EQUALMARK':([79,81,82,83,84,85,86,],[91,-60,-61,-62,-63,-64,-65,]),'SECRULE_ACTION_CTLACTIONARG':([91,],[98,]),'SECRULE_ACTION_INITCOLACTIONARGPARAM':([91,],[99,]),'SEMICOLON':([97,98,99,],[103,-69,-70,]),'SECRULE_ACTION_CTLACTIONARGPARAM':([103,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'modsec_config':([0,],[1,]),'comment_line':([0,1,],[2,19,]),'secrule_line':([0,1,],[3,20,]),'seccompsignature_line':([0,1,],[4,18,]),'secaction_line':([0,1,],[5,16,]),'secmarker_line':([0,1,],[6,17,]),'tok_confdir_secrule':([0,1,],[8,8,]),'tok_confdir_secaction':([0,1,],[10,10,]),'secmarker_line_quoted':([0,1,],[11,11,]),'secmarker_line_noquoted':([0,1,],[12,12,]),'secvariable_expr_list':([8,],[21,]),'secvariable_expr':([8,37,38,],[22,58,59,]),'tok_secrule_variable':([8,28,37,38,],[23,42,23,23,]),'tok_secrule_variable_prefix':([8,37,38,],[24,24,24,]),'tok_secrule_variable_with_arg':([8,37,38,],[25,25,25,]),'tok_secrule_variable_prefix_with_arg':([8,37,38,],[26,26,26,]),'secvariable_prefix':([8,37,38,],[28,28,28,]),'secoperatorarg_noquote':([21,],[36,]),'tok_secrule_variable_colon':([23,42,],[40,65,]),'secaction_expr_list':([32,57,87,],[45,75,96,]),'secaction_expr':([32,57,68,87,],[46,46,78,46,]),'tok_secrule_action':([32,57,68,87,],[47,47,47,47,]),'secoperator_expr':([35,],[50,]),'tok_secoperator_group':([35,],[51,]),'secoperator_arg_group':([35,51,],[52,72,]),'secvariable_arg':([40,65,],[60,77,]),'tok_secrule_variable_arg':([40,65,],[61,61,]),'tok_secrule_variable_arg_quotes':([40,65,],[62,62,]),'secrule_action_argument':([69,],[79,]),'secrule_action_argument_singlequoted':([80,],[92,]),'tok_secrule_action_ctlactionarg':([91,],[97,]),'tok_secrule_action_ctlactionargparam':([103,],[104,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> modsec_config","S'",1,None,None,None),
  ('modsec_config -> comment_line','modsec_config',1,'p_config_line','msc_pyparser.py',393),
  ('modsec_config -> secrule_line','modsec_config',1,'p_config_line','msc_pyparser.py',394),
  ('modsec_config -> seccompsignature_line','modsec_config',1,'p_config_line','msc_pyparser.py',395),
  ('modsec_config -> secaction_line','modsec_config',1,'p_config_line','msc_pyparser.py',396),
  ('modsec_config -> modsec_config secaction_line','modsec_config',2,'p_config_line','msc_pyparser.py',397),
  ('modsec_config -> secmarker_line','modsec_config',1,'p_config_line','msc_pyparser.py',398),
  ('modsec_config -> modsec_config secmarker_line','modsec_config',2,'p_config_line','msc_pyparser.py',399),
  ('modsec_config -> modsec_config seccompsignature_line','modsec_config',2,'p_config_line','msc_pyparser.py',400),
  ('modsec_config -> modsec_config comment_line','modsec_config',2,'p_config_line','msc_pyparser.py',401),
  ('modsec_config -> modsec_config secrule_line','modsec_config',2,'p_config_line','msc_pyparser.py',402),
  ('comment_line -> COMMENT','comment_line',1,'p_comment_line','msc_pyparser.py',404),
  ('seccompsignature_line -> CONFDIR_SECCOMPSIGNATURE QUOTED SECCOMPSIGNARG QUOTED','seccompsignature_line',4,'p_seccompsignaure_line','msc_pyparser.py',409),
  ('secaction_line -> tok_confdir_secaction QUOTED secaction_expr_list QUOTED','secaction_line',4,'p_secaction_line','msc_pyparser.py',417),
  ('tok_confdir_secaction -> CONFDIR_SECACTION','tok_confdir_secaction',1,'p_tok_confdir_secaction','msc_pyparser.py',421),
  ('secmarker_line -> secmarker_line_quoted','secmarker_line',1,'p_secmarker_line','msc_pyparser.py',431),
  ('secmarker_line -> secmarker_line_noquoted','secmarker_line',1,'p_secmarker_line','msc_pyparser.py',432),
  ('secmarker_line_quoted -> CONFDIR_SECMARKER QUOTED SECMARKERARG QUOTED','secmarker_line_quoted',4,'p_secmarker_line_quoted','msc_pyparser.py',436),
  ('secmarker_line_noquoted -> CONFDIR_SECMARKER SECMARKERARG','secmarker_line_noquoted',2,'p_secmarker_line_noquoted','msc_pyparser.py',440),
  ('secrule_line -> tok_confdir_secrule secvariable_expr_list QUOTED secoperator_expr QUOTED QUOTED secaction_expr_list QUOTED','secrule_line',8,'p_secrule_line','msc_pyparser.py',448),
  ('secrule_line -> tok_confdir_secrule secvariable_expr_list QUOTED secoperator_expr QUOTED','secrule_line',5,'p_secrule_line','msc_pyparser.py',449),
  ('secrule_line -> tok_confdir_secrule secvariable_expr_list secoperatorarg_noquote QUOTED secaction_expr_list QUOTED','secrule_line',6,'p_secrule_line','msc_pyparser.py',450),
  ('secrule_line -> tok_confdir_secrule secvariable_expr_list secoperatorarg_noquote','secrule_line',3,'p_secrule_line','msc_pyparser.py',451),
  ('tok_confdir_secrule -> CONFDIR_SECRULE','tok_confdir_secrule',1,'p_tok_confdir_secrule','msc_pyparser.py',455),
  ('secvariable_expr_list -> secvariable_expr','secvariable_expr_list',1,'p_secvariable_expr_list','msc_pyparser.py',460),
  ('secvariable_expr_list -> secvariable_expr_list PIPE secvariable_expr','secvariable_expr_list',3,'p_secvariable_expr_list','msc_pyparser.py',461),
  ('secvariable_expr_list -> secvariable_expr_list COMMA secvariable_expr','secvariable_expr_list',3,'p_secvariable_expr_list','msc_pyparser.py',462),
  ('secvariable_expr -> tok_secrule_variable','secvariable_expr',1,'p_secvariable_expr','msc_pyparser.py',466),
  ('secvariable_expr -> tok_secrule_variable_prefix','secvariable_expr',1,'p_secvariable_expr','msc_pyparser.py',467),
  ('secvariable_expr -> tok_secrule_variable_with_arg','secvariable_expr',1,'p_secvariable_expr','msc_pyparser.py',468),
  ('secvariable_expr -> tok_secrule_variable_prefix_with_arg','secvariable_expr',1,'p_secvariable_expr','msc_pyparser.py',469),
  ('tok_secrule_variable -> SECRULE_VARIABLE','tok_secrule_variable',1,'p_tok_secrule_variable','msc_pyparser.py',474),
  ('tok_secrule_variable_prefix -> secvariable_prefix tok_secrule_variable','tok_secrule_variable_prefix',2,'p_tok_secrule_variable_prefix','msc_pyparser.py',478),
  ('tok_secrule_variable_with_arg -> tok_secrule_variable tok_secrule_variable_colon secvariable_arg','tok_secrule_variable_with_arg',3,'p_tok_secrule_variable_with_arg','msc_pyparser.py',482),
  ('tok_secrule_variable_prefix_with_arg -> secvariable_prefix tok_secrule_variable tok_secrule_variable_colon secvariable_arg','tok_secrule_variable_prefix_with_arg',4,'p_tok_secrule_variable_prefix_with_arg','msc_pyparser.py',486),
  ('tok_secrule_variable_colon -> COLON','tok_secrule_variable_colon',1,'p_tok_secrule_variable_colon','msc_pyparser.py',490),
  ('secvariable_prefix -> AND','secvariable_prefix',1,'p_secvariable_prefix','msc_pyparser.py',494),
  ('secvariable_prefix -> EXCLAMMARK','secvariable_prefix',1,'p_secvariable_prefix','msc_pyparser.py',495),
  ('secvariable_prefix -> EXCLAMMARK AND','secvariable_prefix',2,'p_secvariable_prefix','msc_pyparser.py',496),
  ('secvariable_arg -> tok_secrule_variable_arg','secvariable_arg',1,'p_secvariable_arg','msc_pyparser.py',500),
  ('secvariable_arg -> tok_secrule_variable_arg_quotes','secvariable_arg',1,'p_secvariable_arg','msc_pyparser.py',501),
  ('tok_secrule_variable_arg -> SECRULE_VARIABLE_ARG','tok_secrule_variable_arg',1,'p_tok_secrule_variable_arg','msc_pyparser.py',505),
  ('tok_secrule_variable_arg_quotes -> QUOTES SECRULE_VARIABLE_ARG QUOTES','tok_secrule_variable_arg_quotes',3,'p_tok_secrule_variable_arg_quotes','msc_pyparser.py',509),
  ('secoperator_expr -> tok_secoperator_group','secoperator_expr',1,'p_secoperator_expr','msc_pyparser.py',513),
  ('secoperator_expr -> tok_secoperator_group secoperator_arg_group','secoperator_expr',2,'p_secoperator_expr','msc_pyparser.py',514),
  ('secoperator_expr -> secoperator_arg_group','secoperator_expr',1,'p_secoperator_expr','msc_pyparser.py',515),
  ('tok_secoperator_group -> ATSIGN SECRULE_OPERATOR','tok_secoperator_group',2,'p_tok_secoperator_group','msc_pyparser.py',519),
  ('tok_secoperator_group -> EXCLAMMARK ATSIGN SECRULE_OPERATOR','tok_secoperator_group',3,'p_tok_secoperator_group','msc_pyparser.py',520),
  ('tok_secoperator_group -> EXCLAMMARK','tok_secoperator_group',1,'p_tok_secoperator_group','msc_pyparser.py',521),
  ('secoperator_arg_group -> SECRULE_OPERATOR_ARG','secoperator_arg_group',1,'p_secoperator_arg_group','msc_pyparser.py',526),
  ('secoperator_arg_group -> NUMBER','secoperator_arg_group',1,'p_secoperator_arg_group','msc_pyparser.py',527),
  ('secoperatorarg_noquote -> SECRULE_OPERATOR_ARG_NOQUOTE','secoperatorarg_noquote',1,'p_secoperatorarg_noquote','msc_pyparser.py',531),
  ('secaction_expr_list -> secaction_expr','secaction_expr_list',1,'p_secaction_expr_list','msc_pyparser.py',536),
  ('secaction_expr_list -> secaction_expr_list COMMA secaction_expr','secaction_expr_list',3,'p_secaction_expr_list','msc_pyparser.py',537),
  ('secaction_expr -> tok_secrule_action','secaction_expr',1,'p_secaction_expr','msc_pyparser.py',541),
  ('secaction_expr -> tok_secrule_action COLON secrule_action_argument','secaction_expr',3,'p_secaction_expr','msc_pyparser.py',542),
  ('secaction_expr -> tok_secrule_action COLON QUOTES secrule_action_argument_singlequoted QUOTES','secaction_expr',5,'p_secaction_expr','msc_pyparser.py',543),
  ('secaction_expr -> tok_secrule_action COLON secrule_action_argument EQUALMARK tok_secrule_action_ctlactionarg','secaction_expr',5,'p_secaction_expr','msc_pyparser.py',544),
  ('secaction_expr -> tok_secrule_action COLON secrule_action_argument EQUALMARK tok_secrule_action_ctlactionarg SEMICOLON tok_secrule_action_ctlactionargparam','secaction_expr',7,'p_secaction_expr','msc_pyparser.py',545),
  ('tok_secrule_action -> SECRULE_ACTION','tok_secrule_action',1,'p_tok_secrule_action','msc_pyparser.py',549),
  ('secrule_action_argument -> SECRULE_ACTION_ARG','secrule_action_argument',1,'p_secrule_action_argument','msc_pyparser.py',558),
  ('secrule_action_argument -> NUMBER','secrule_action_argument',1,'p_secrule_action_argument','msc_pyparser.py',559),
  ('secrule_action_argument -> SECRULE_ACTION_TRANSFORMS','secrule_action_argument',1,'p_secrule_action_argument','msc_pyparser.py',560),
  ('secrule_action_argument -> SECRULE_ACTION_CTLACTION','secrule_action_argument',1,'p_secrule_action_argument','msc_pyparser.py',561),
  ('secrule_action_argument -> SECRULE_ACTION_SKIPAFTERACTIONARG','secrule_action_argument',1,'p_secrule_action_argument','msc_pyparser.py',562),
  ('secrule_action_argument -> SECRULE_ACTION_INITCOLACTIONARG','secrule_action_argument',1,'p_secrule_action_argument','msc_pyparser.py',563),
  ('secrule_action_argument_singlequoted -> SECRULE_ACTION_ARG','secrule_action_argument_singlequoted',1,'p_secrule_action_argument_singlequoted','msc_pyparser.py',570),
  ('secrule_action_argument_singlequoted -> EXCLAMMARK SECRULE_ACTION_ARG','secrule_action_argument_singlequoted',2,'p_secrule_action_argument_singlequoted','msc_pyparser.py',571),
  ('secrule_action_argument_singlequoted -> NUMBER','secrule_action_argument_singlequoted',1,'p_secrule_action_argument_singlequoted','msc_pyparser.py',572),
  ('tok_secrule_action_ctlactionarg -> SECRULE_ACTION_CTLACTIONARG','tok_secrule_action_ctlactionarg',1,'p_tok_secrule_action_ctlactionarg','msc_pyparser.py',581),
  ('tok_secrule_action_ctlactionarg -> SECRULE_ACTION_INITCOLACTIONARGPARAM','tok_secrule_action_ctlactionarg',1,'p_tok_secrule_action_ctlactionarg','msc_pyparser.py',582),
  ('tok_secrule_action_ctlactionargparam -> SECRULE_ACTION_CTLACTIONARGPARAM','tok_secrule_action_ctlactionargparam',1,'p_tok_secrule_action_ctlactionargparam','msc_pyparser.py',589),
]
