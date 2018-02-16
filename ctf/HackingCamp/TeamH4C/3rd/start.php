line     #* E I O op                           fetch          ext  return  operands
——————————————————————————————————————————
   2     0  E >   INCLUDE_OR_EVAL                                          '.%2Fconfig.php', INCLUDE
   4     1        ASSIGN                                                   !0, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
   5     2        INIT_FCALL                                               'rand'
         3        SEND_VAL                                                 0
         4        STRLEN                                           ~9      !0
         5        SEND_VAL                                                 ~9
         6        DO_ICALL                                         $10     
         7        FETCH_DIM_R                                      $11     !0, $10
         8        ASSIGN                                                   !1, $11
   6     9        INIT_FCALL                                               'rand'
        10        SEND_VAL                                                 0
        11        STRLEN                                           ~13     !0
        12        SEND_VAL                                                 ~13
        13        DO_ICALL                                         $14     
        14        FETCH_DIM_R                                      $15     !0, $14
        15        ASSIGN                                                   !2, $15
   7    16        INIT_FCALL                                               'rand'
        17        SEND_VAL                                                 0
        18        STRLEN                                           ~17     !0
        19        SEND_VAL                                                 ~17
        20        DO_ICALL                                         $18     
        21        FETCH_DIM_R                                      $19     !0, $18
        22        ASSIGN                                                   !3, $19
   9    23        ASSIGN                                                   !4, !5
  10    24        INIT_FCALL                                               'base64_encode'
        25        INIT_FCALL                                               'base64_encode'
        26        SEND_VAR                                                 !4
        27        DO_ICALL                                         $22     
        28        SEND_VAR                                                 $22
        29        DO_ICALL                                         $23     
        30        ASSIGN                                                   !6, $23
  11    31        ASSIGN_DIM                                               !6, 25
        32        OP_DATA                                                  !1
  12    33        ASSIGN_DIM                                               !6, 29
        34        OP_DATA                                                  !2
  13    35        ASSIGN_DIM                                               !6, 27
        36        OP_DATA                                                  !3
  14    37      > JMPZ                                                     1, ->216
        38    >   FETCH_R                      global              $28     '_GET'
        39        FETCH_DIM_R                                      $29     $28, 'view'
        40        CONCAT                                           ~30     'camp', $29
        41        IS_NOT_IDENTICAL                                 ~31     ~30, 'i_want_flag'
        42      > JMPNZ_EX                                         ~31     ~31, ->102
        43    >   FETCH_R                      global              $32     '_GET'
        44        FETCH_DIM_R                                      $33     $32, 'view'
        45        INIT_FCALL                                               'sha1'
        46        INIT_FCALL                                               'rand'
        47        SEND_VAL                                                 0
        48        SEND_VAL                                                 255
        49        DO_ICALL                                         $34     
        50        INIT_FCALL                                               'rand'
        51        SEND_VAL                                                 0
        52        SEND_VAL                                                 255
        53        DO_ICALL                                         $35     
        54        CONCAT                                           ~36     $34, $35
        55        SEND_VAL                                                 ~36
        56        DO_ICALL                                         $37     
        57        INIT_FCALL                                               'uniqid'
        58        INIT_FCALL                                               'rand'
        59        SEND_VAL                                                 0
        60        SEND_VAL                                                 255
        61        DO_ICALL                                         $38     
        62        INIT_FCALL                                               'rand'
        63        SEND_VAL                                                 0
        64        SEND_VAL                                                 255
        65        DO_ICALL                                         $39     
        66        CONCAT                                           ~40     $38, $39
        67        SEND_VAL                                                 ~40
        68        DO_ICALL                                         $41     
        69        CONCAT                                           ~42     $37, $41
        70        INIT_FCALL                                               'md5'
        71        INIT_FCALL                                               'rand'
        72        SEND_VAL                                                 0
        73        SEND_VAL                                                 255
        74        DO_ICALL                                         $43     
        75        INIT_FCALL                                               'rand'
        76        SEND_VAL                                                 0
        77        SEND_VAL                                                 255
        78        DO_ICALL                                         $44     
        79        CONCAT                                           ~45     $43, $44
        80        SEND_VAL                                                 ~45
        81        DO_ICALL                                         $46     
        82        CONCAT                                           ~47     ~42, $46
        83        INIT_FCALL                                               'md5'
        84        INIT_FCALL                                               'rand'
        85        SEND_VAL                                                 0
        86        SEND_VAL                                                 255
        87        DO_ICALL                                         $48     
        88        INIT_FCALL                                               'rand'
        89        SEND_VAL                                                 0
        90        SEND_VAL                                                 255
        91        DO_ICALL                                         $49     
        92        CONCAT                                           ~50     $48, $49
        93        SEND_VAL                                                 ~50
        94        DO_ICALL                                         $51     
        95        CONCAT                                           ~52     ~47, $51
        96        INIT_FCALL                                               'uniqid'
        97        SEND_VAL                                                 'we1c0me_t0_myung_yong_world'
        98        DO_ICALL                                         $53     
        99        CONCAT                                           ~54     ~52, $53
       100        IS_NOT_IDENTICAL                                 ~55     $33, ~54
       101        BOOL                                             ~31     ~55
       102    > > JMPZ                                                     ~31, ->215
       103    >   FETCH_R                      global              $56     '_GET'
       104        FETCH_DIM_R                                      $57     $56, 'view'
       105        FETCH_DIM_R                                      $58     $57, 0
       106        IS_EQUAL                                         ~59     $58, 'hi'
       107      > JMPZ                                                     ~59, ->214
       108    >   INIT_FCALL                                               'strstr'
       109        FETCH_R                      global              $60     '_GET'
       110        FETCH_DIM_R                                      $61     $60, 'view'
       111        FETCH_DIM_R                                      $62     $61, 0
       112        SEND_VAR                                                 $62
       113        INIT_FCALL                                               'strtolower'
       114        SEND_VAL                                                 'H'
       115        DO_ICALL                                         $63     
       116        SEND_VAR                                                 $63
       117        DO_ICALL                                         $64     
       118      > JMPZ                                                     $64, ->214
       119    >   INIT_FCALL                                               'chr'
       120        FETCH_R                      global              $65     '_GET'
       121        FETCH_DIM_R                                      $66     $65, 'view'
       122        FETCH_DIM_R                                      $67     $66, 0
       123        SEND_VAR                                                 $67
       124        DO_ICALL                                         $68     
       125        IS_SMALLER_OR_EQUAL                              ~69     $68, 0
       126      > JMPZ                                                     ~69, ->214
       127    >   FETCH_R                      global              $70     '_GET'
       128        FETCH_DIM_R                                      $71     $70, 'view'
       129        FETCH_DIM_R                                      $72     $71, 3
       130        IS_NOT_IDENTICAL                                 ~73     $72, 'iphone'
       131      > JMPZ                                                     ~73, ->214
       132    >   INIT_FCALL                                               'chr'
       133        FETCH_R                      global              $74     '_GET'
       134        FETCH_DIM_R                                      $75     $74, 'view'
       135        FETCH_DIM_R                                      $76     $75, 1
       136        BW_XOR                                           ~77     $76, 97
       137        SEND_VAL                                                 ~77
       138        DO_ICALL                                         $78     
       139        INIT_FCALL                                               'chr'
       140        FETCH_R                      global              $79     '_GET'
       141        FETCH_DIM_R                                      $80     $79, 'view'
       142        FETCH_DIM_R                                      $81     $80, 2
       143        BW_XOR                                           ~82     $81, 60
       144        SEND_VAL                                                 ~82
       145        DO_ICALL                                         $83     
       146        IS_EQUAL                                         ~84     $78, $83
       147      > JMPZ                                                     ~84, ->214
       148    >   FETCH_R                      global              $85     '_GET'
       149        FETCH_DIM_R                                      $86     $85, 'view'
       150        FETCH_DIM_R                                      $87     $86, 3
       151        IS_IDENTICAL                                     ~88     $87, 'iph0ne'
       152      > JMPZ                                                     ~88, ->214
       153    >   FETCH_R                      global              $89     '_GET'
       154        FETCH_DIM_R                                      $90     $89, 'view'
       155        IS_NOT_IDENTICAL                                 ~91     $90, '%24_GET%5B%27view%27%5D%5B4%5D'
       156      > JMPZ                                                     ~91, ->214
       157    >   INIT_FCALL                                               'str_replace'
       158        SEND_VAL                                                 
       159        SEND_VAL                                                 ''
       160        FETCH_R                      global              $92     '_GET'
       161        FETCH_DIM_R                                      $93     $92, 'view'
       162        FETCH_DIM_R                                      $94     $93, 4
       163        SEND_VAR                                                 $94
       164        DO_ICALL                                         $95     
       165        IS_EQUAL                                         ~96     $95, 'lee_myung_yong'
       166      > JMPZ                                                     ~96, ->214
       167    >   FETCH_R                      global              $97     '_GET'
       168        FETCH_DIM_R                                      $98     $97, 'view'
       169        FETCH_DIM_R                                      $99     $98, 4
       170        FETCH_DIM_R                                      $100    $99, 1
       171        IS_NOT_IDENTICAL                                 ~101    $100, 'e'
       172      > JMPZ                                                     ~101, ->214
       173    >   FETCH_R                      global              $102    '_GET'
       174        FETCH_DIM_R                                      $103    $102, 'view'
       175        FETCH_DIM_R                                      $104    $103, 4
       176        FETCH_DIM_R                                      $105    $104, 8
       177        IS_IDENTICAL                                     ~106    $105, 'e'
       178      > JMPZ                                                     ~106, ->214
       179    >   FETCH_R                      global              $107    '_GET'
       180        FETCH_DIM_R                                      $108    $107, 'view'
       181        FETCH_DIM_R                                      $109    $108, 9
       182        FETCH_DIM_R                                      $110    $109, 8
       183        FETCH_DIM_R                                      $111    $110, 7
       184        FETCH_DIM_R                                      $112    $111, 4
       185        FETCH_DIM_R                                      $113    $112, 5
       186        FETCH_DIM_R                                      $114    $113, 6
       187        FETCH_DIM_R                                      $115    $114, 'le'
       188        FETCH_DIM_R                                      $116    $115, 'my'
       189        FETCH_DIM_R                                      $117    $116, 'yo'
       190        IS_EQUAL                                         ~118    $117, '123%21%40%23'
       191      > JMPZ                                                     ~118, ->214
       192    >   FETCH_R                      global              $119    '_GET'
       193        FETCH_DIM_R                                      $120    $119, 'view'
       194        FETCH_DIM_R                                      $121    $120, 5
       195        SUB                                              ~122    $121, 1
       196        IS_EQUAL                                         ~123    ~122, '3'
       197      > JMPZ                                                     ~123, ->214
       198    >   BEGIN_SILENCE                                    ~124    
       199        INIT_FCALL                                               'md5'
       200        FETCH_R                      global              $125    '_GET'
       201        FETCH_DIM_R                                      $126    $125, 'view'
       202        FETCH_DIM_R                                      $127    $126, 6
       203        ADD                                              ~128    $127, 291
       204        SEND_VAL                                                 ~128
       205        DO_ICALL                                         $129    
       206        END_SILENCE                                              ~124
       207        INIT_FCALL                                               'md5'
       208        CAST                                          6  ~130    240610708
       209        SEND_VAL                                                 ~130
       210        DO_ICALL                                         $131    
       211        IS_EQUAL                                         ~132    $129, $131
       212      > JMPZ                                                     ~132, ->214
       213    >   ECHO                                                     !6
       214    > > JMP                                                      ->216
  15   215    >   ECHO                                                     !6
  16   216    > > RETURN                                                   1