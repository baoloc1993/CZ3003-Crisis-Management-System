
      function initialize() {

        //Initializing the map
        var mapOptions = {
          center: new google.maps.LatLng(1.377278, 103.797798),
          zoom: 11
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
        //Defining the region coordinates
        var southWestCoords_1,southWestCoords_2,northWestCoords,centralSingaporeCoords, northEastCoords, SouthEastCoords;
        var southWestBound_1,southWestBound_2,northWestBound,centralSingaporeBound, northEastBound, SouthEastBound;
        
        var southWestCoords_1 = [
         	  new google.maps.LatLng(1.4366551582477902, 103.75316619873047),
                  new google.maps.LatLng(1.431850145552487, 103.75110626220703),
                  new google.maps.LatLng(1.4109139016955707, 103.7552261352539),
                  new google.maps.LatLng(1.4040495182936055, 103.75213623046875),
                  new google.maps.LatLng(1.3889478039948222, 103.75385284423828),
                  new google.maps.LatLng(1.3807104645408492, 103.75934600830078),
                  new google.maps.LatLng(1.3635492491975707, 103.76724243164062),
                  new google.maps.LatLng(1.3573711816421556, 103.74183654785156),
                  new google.maps.LatLng(1.3196159840368622, 103.77204895019531),
                  new google.maps.LatLng(1.3161836646805007, 103.76724243164062),
                  new google.maps.LatLng(1.2880384688779298, 103.78646850585938),
                  new google.maps.LatLng(1.2839196334992269, 103.80775451660156),
                  new google.maps.LatLng(1.2605794416293021, 103.8043212890625),
                  new google.maps.LatLng(1.259206482612979, 103.81942749023438),
                  new google.maps.LatLng(1.2646983143314323, 103.83522033691406),
                  new google.maps.LatLng(1.2571470427328022, 103.84140014648438),
                  new google.maps.LatLng(1.2468498190181676, 103.84757995605469),
                  new google.maps.LatLng(1.220763339430388, 103.8592529296875),
                  new google.maps.LatLng(1.213211942600496, 103.85169982910156),
                  new google.maps.LatLng(1.2564605624116145, 103.80294799804688),
                  new google.maps.LatLng(1.2564605624116145, 103.78509521484375),
                  new google.maps.LatLng(1.259206482612979, 103.77754211425781),
                  new google.maps.LatLng(1.2732792781077762, 103.78646850585938),
                  new google.maps.LatLng(1.2794575543509612, 103.77788543701172),
                  new google.maps.LatLng(1.2684739418998092, 103.7710189819336),
                  new google.maps.LatLng(1.2798007914844112, 103.7497329711914),
                  new google.maps.LatLng(1.287008760656557, 103.75625610351562),
                  new google.maps.LatLng(1.2801440285719212, 103.7662124633789),
                  new google.maps.LatLng(1.2839196334992269, 103.7713623046875),
                  new google.maps.LatLng(1.290784355433135, 103.7607192993164),
                  new google.maps.LatLng(1.3055434447085699, 103.7552261352539),
                  new google.maps.LatLng(1.310348710939347, 103.74767303466797),
                  new google.maps.LatLng(1.3185862887267221, 103.7435531616211),
                  new google.maps.LatLng(1.3185862887267221, 103.73634338378906),
                  new google.maps.LatLng(1.30863254548484, 103.73908996582031),
                  new google.maps.LatLng(1.3038272759699876, 103.74732971191406),
                  new google.maps.LatLng(1.3045137436059018, 103.75144958496094),
                  new google.maps.LatLng(1.2973058241064253, 103.75213623046875),
                  new google.maps.LatLng(1.2979922935167072, 103.7442398071289),
                  new google.maps.LatLng(1.3003949349844677, 103.72913360595703),
                  new google.maps.LatLng(1.29902199728267, 103.71334075927734),
                  new google.maps.LatLng(1.29902199728267, 103.68415832519531),
                  new google.maps.LatLng(1.2887249407943744, 103.66630554199219),
                  new google.maps.LatLng(1.3151539679518205, 103.63815307617188),
                  new google.maps.LatLng(1.3110351767920259, 103.63471984863281),
                  new google.maps.LatLng(1.2828899236168412, 103.6501693725586),
                  new google.maps.LatLng(1.278771079946305, 103.64673614501953),
                  new google.maps.LatLng(1.2801440285719212, 103.64227294921875),
                  new google.maps.LatLng(1.2650415534284933, 103.6391830444336),
                  new google.maps.LatLng(1.252341676699629, 103.61515045166016),
                  new google.maps.LatLng(1.2382687684731497, 103.6227035522461),
                  new google.maps.LatLng(1.2372390405371851, 103.6172103881836),
                  new google.maps.LatLng(1.2399849808106485, 103.61068725585938),
                  new google.maps.LatLng(1.2434174021459743, 103.60553741455078),
                  new google.maps.LatLng(1.2554308415916193, 103.61103057861328),
                  new google.maps.LatLng(1.2616091604165158, 103.6065673828125),
                  new google.maps.LatLng(1.277398130586286, 103.6124038696289),
                  new google.maps.LatLng(1.2897546483220683, 103.61995697021484),
                  new google.maps.LatLng(1.2938734742631495, 103.61618041992188),
                  new google.maps.LatLng(1.344671771064049, 103.63471984863281),
                  new google.maps.LatLng(1.3511930983018765, 103.63815307617188),
                  new google.maps.LatLng(1.341925943851875, 103.64879608154297),
                  new google.maps.LatLng(1.3350613623490613, 103.65325927734375),
                  new google.maps.LatLng(1.3378071972557988, 103.65806579589844),
                  new google.maps.LatLng(1.3553118222790563, 103.64158630371094),
                  new google.maps.LatLng(1.3614898951040653, 103.6501693725586),
                  new google.maps.LatLng(1.374532441208973, 103.65325927734375),
                  new google.maps.LatLng(1.37178664792646, 103.66802215576172),
                  new google.maps.LatLng(1.3755621128762436, 103.6724853515625),
                  new google.maps.LatLng(1.3831130248377372, 103.65875244140625),
                  new google.maps.LatLng(1.4061088354351594, 103.66355895996094),
                  new google.maps.LatLng(1.4256722572915292, 103.67523193359375),
                  new google.maps.LatLng(1.4438626583311722, 103.7051010131836),
                  new google.maps.LatLng(1.450383710146488, 103.72055053710938),
                  new google.maps.LatLng(1.4490108586915245, 103.72947692871094),
                  new google.maps.LatLng(1.442146588951299, 103.7380599975586),
                  new google.maps.LatLng(1.4335662226731178, 103.73703002929688),
                  new google.maps.LatLng(1.4232697407088972, 103.73565673828125),
                  new google.maps.LatLng(1.4143460858068722, 103.7277603149414),
                  new google.maps.LatLng(1.4109139016955707, 103.72501373291016),
                  new google.maps.LatLng(1.404392737943241, 103.7277603149414),
                  new google.maps.LatLng(1.4157189580307559, 103.73531341552734),
                  new google.maps.LatLng(1.4242993909796224, 103.7435531616211),
                  new google.maps.LatLng(1.4404305182774741, 103.74286651611328)        
        ];

        var southWestCoords_2 = [
                  new google.maps.LatLng(1.2894114125257743, 103.6834716796875),
                  new google.maps.LatLng(1.2719063258180718, 103.65617752075195),
                  new google.maps.LatLng(1.2435890230956916, 103.66888046264648),
                  new google.maps.LatLng(1.24255929723009, 103.66561889648438),
                  new google.maps.LatLng(1.2346647189493931, 103.66939544677734),
                  new google.maps.LatLng(1.234321475882542, 103.67300033569336),
                  new google.maps.LatLng(1.2267701172247893, 103.67609024047852),
                  new google.maps.LatLng(1.2252255185058678, 103.67042541503906),
                  new google.maps.LatLng(1.2229944298954822, 103.67471694946289),
                  new google.maps.LatLng(1.230030933812843, 103.68192672729492),
                  new google.maps.LatLng(1.2375822832269368, 103.68879318237305),
                  new google.maps.LatLng(1.2576619028552396, 103.6863899230957),
                  new google.maps.LatLng(1.2636685967679053, 103.68038177490234),
                  new google.maps.LatLng(1.2681307032573512, 103.68518829345703),
                  new google.maps.LatLng(1.2595497224348884, 103.69342803955078),
                  new google.maps.LatLng(1.2502822314149262, 103.69583129882812),
                  new google.maps.LatLng(1.259034862685072, 103.7138557434082),
                  new google.maps.LatLng(1.2660712704472168, 103.70475769042969),
                  new google.maps.LatLng(1.2681307032573512, 103.70681762695312),
                  new google.maps.LatLng(1.2604078217918373, 103.72312545776367),
                  new google.maps.LatLng(1.2634969771342888, 103.7303352355957),
                  new google.maps.LatLng(1.2689887997780853, 103.72570037841797),
                  new google.maps.LatLng(1.2700185152271923, 103.73308181762695),
                  new google.maps.LatLng(1.2737941350279294, 103.74063491821289),
                  new google.maps.LatLng(1.278084605358042, 103.73497009277344),
                  new google.maps.LatLng(1.2837480152143055, 103.72673034667969),
                  new google.maps.LatLng(1.291814062127231, 103.71866226196289),
                  new google.maps.LatLng(1.2919856798690028, 103.7105941772461),
                  new google.maps.LatLng(1.2906127376102337, 103.70424270629883),
                  new google.maps.LatLng(1.2828899236168412, 103.70630264282227),
                  new google.maps.LatLng(1.278771079946305, 103.70698928833008),
                  new google.maps.LatLng(1.284949342966881, 103.70063781738281),
                  new google.maps.LatLng(1.272936040103872, 103.68793487548828),
                  new google.maps.LatLng(1.2765400368637023, 103.68432998657227),
                  new google.maps.LatLng(1.290097884072066, 103.69565963745117),
                  new google.maps.LatLng(1.2902695019296992, 103.68810653686523),
        ];

        var northWestCoords = [
                  new google.maps.LatLng(1.3227050674082719, 103.77239227294922),
                  new google.maps.LatLng(1.3573711816421556, 103.74286651611328),
                  new google.maps.LatLng(1.3635492491975707, 103.76655578613281),
                  new google.maps.LatLng(1.378651125210677, 103.76106262207031),
                  new google.maps.LatLng(1.3886045820896773, 103.75556945800781),
                  new google.maps.LatLng(1.4037062985935518, 103.75316619873047),
                  new google.maps.LatLng(1.410055854876029, 103.75505447387695),
                  new google.maps.LatLng(1.4304772829308758, 103.75144958496094),
                  new google.maps.LatLng(1.4375131951666087, 103.75299453735352),
                  new google.maps.LatLng(1.438028017163139, 103.76174926757812),
                  new google.maps.LatLng(1.445750333152633, 103.76775741577148),
                  new google.maps.LatLng(1.4515849544863708, 103.7771987915039),
                  new google.maps.LatLng(1.4659998366350788, 103.79779815673828),
                  new google.maps.LatLng(1.469431937786789, 103.81032943725586),
                  new google.maps.LatLng(1.4690887279087208, 103.82183074951172),
                  new google.maps.LatLng(1.4659998366350788, 103.82183074951172),
                  new google.maps.LatLng(1.4659998366350788, 103.82492065429688),
                  new google.maps.LatLng(1.4680590979582542, 103.82766723632812),
                  new google.maps.LatLng(1.464283784085403, 103.83401870727539),
                  new google.maps.LatLng(1.463597362697591, 103.83848190307617),
                  new google.maps.LatLng(1.4603368582377747, 103.84191513061523),
                  new google.maps.LatLng(1.4555318956783565, 103.85015487670898),
                  new google.maps.LatLng(1.452442985767033, 103.85221481323242),
                  new google.maps.LatLng(1.4500404973607948, 103.8482666015625),
                  new google.maps.LatLng(1.4514133481911609, 103.84603500366211),
                  new google.maps.LatLng(1.448152826109596, 103.84586334228516),
                  new google.maps.LatLng(1.448324432651973, 103.85255813598633),
                  new google.maps.LatLng(1.4495256780846946, 103.85770797729492),
                  new google.maps.LatLng(1.4438626583311722, 103.86320114135742),
                  new google.maps.LatLng(1.4378564098438669, 103.86577606201172),
                  new google.maps.LatLng(1.4419749819421182, 103.86028289794922),
                  new google.maps.LatLng(1.4399156968232156, 103.85753631591797),
                  new google.maps.LatLng(1.4347674758923208, 103.86320114135742),
                  new google.maps.LatLng(1.4282463794191294, 103.8589096069336),
                  new google.maps.LatLng(1.4196659611430904, 103.85444641113281),
                  new google.maps.LatLng(1.4122867759484576, 103.84912490844727),
                  new google.maps.LatLng(1.4102274642652444, 103.84654998779297),
                  new google.maps.LatLng(1.413316431105927, 103.83934020996094),
                  new google.maps.LatLng(1.4176066560109675, 103.83350372314453),
                  new google.maps.LatLng(1.4037062985935518, 103.8094711303711),
                  new google.maps.LatLng(1.374189217221201, 103.82389068603516),
                  new google.maps.LatLng(1.369384076219154, 103.8262939453125),
                  new google.maps.LatLng(1.3656086015292142, 103.82801055908203),
                  new google.maps.LatLng(1.3611466692507197, 103.82801055908203),
                  new google.maps.LatLng(1.3604602173974556, 103.82217407226562),
                  new google.maps.LatLng(1.3580576343735706, 103.81805419921875),
                  new google.maps.LatLng(1.3652653762630753, 103.81050109863281),
                  new google.maps.LatLng(1.360631830379095, 103.80123138427734),
                  new google.maps.LatLng(1.3395233425123458, 103.80603790283203),
                                  ];
                
                  

                  var centralSingaporeCoords = [
                  new google.maps.LatLng(1.3213321419396256, 103.7713623046875),
                  new google.maps.LatLng(1.3178998249499785, 103.7662124633789),
                  new google.maps.LatLng(1.2880384688779298, 103.78561019897461),
                  new google.maps.LatLng(1.2840912517726475, 103.80552291870117),
                  new google.maps.LatLng(1.2627246886427133, 103.80560874938965),
                  new google.maps.LatLng(1.265213172960014, 103.80775451660156),
                  new google.maps.LatLng(1.2648699338856497, 103.81024360656738),
                  new google.maps.LatLng(1.262553068946758, 103.81144523620605),
                  new google.maps.LatLng(1.2631537378330235, 103.81324768066406),
                  new google.maps.LatLng(1.2646125045500682, 103.8149642944336),
                  new google.maps.LatLng(1.2631537378330235, 103.81702423095703),
                  new google.maps.LatLng(1.261780780174772, 103.8178825378418),
                  new google.maps.LatLng(1.2626388787961478, 103.82440567016602),
                  new google.maps.LatLng(1.2674442258359135, 103.8321304321289),
                  new google.maps.LatLng(1.2674442258359135, 103.83942604064941),
                  new google.maps.LatLng(1.2616949702970497, 103.84603500366211),
                  new google.maps.LatLng(1.2607510614554567, 103.85152816772461),
                  new google.maps.LatLng(1.261523350533132, 103.85238647460938),
                  new google.maps.LatLng(1.2657280314864108, 103.85161399841309),
                  new google.maps.LatLng(1.2728502305957683, 103.85187149047852),
                  new google.maps.LatLng(1.2692462286788084, 103.8577938079834),
                  new google.maps.LatLng(1.2648699338856497, 103.8607120513916),
                  new google.maps.LatLng(1.2653847924801613, 103.86208534240723),
                  new google.maps.LatLng(1.267787464569386, 103.86019706726074),
                  new google.maps.LatLng(1.277398130586286, 103.87212753295898),
                  new google.maps.LatLng(1.2815169764623715, 103.87092590332031),
                  new google.maps.LatLng(1.2858932429475758, 103.8621711730957),
                  new google.maps.LatLng(1.287008760656557, 103.85951042175293),
                  new google.maps.LatLng(1.2820318317315877, 103.8566780090332),
                  new google.maps.LatLng(1.2817744041099053, 103.85461807250977),
                  new google.maps.LatLng(1.2867513335362317, 103.85453224182129),
                  new google.maps.LatLng(1.288939463230321, 103.85783672332764),
                  new google.maps.LatLng(1.2888965587445744, 103.86478900909424),
                  new google.maps.LatLng(1.2978206761816011, 103.86423110961914),
                  new google.maps.LatLng(1.301939489006291, 103.86783599853516),
                  new google.maps.LatLng(1.307173803925156, 103.8644027709961),
                  new google.maps.LatLng(1.354625368768736, 103.85650634765625),
                  new google.maps.LatLng(1.3697273008963304, 103.86114120483398),
                  new google.maps.LatLng(1.3695556885638807, 103.875732421875),
                  new google.maps.LatLng(1.3887761930484837, 103.88105392456055),
                  new google.maps.LatLng(1.4035346887246325, 103.88671875),
                  new google.maps.LatLng(1.4119435574612258, 103.89530181884766),
                  new google.maps.LatLng(1.4201807871396008, 103.89787673950195),
                  new google.maps.LatLng(1.4320217533223802, 103.8783073425293),
                  new google.maps.LatLng(1.4287612034988086, 103.86955261230469),
                  new google.maps.LatLng(1.4224116984654103, 103.86354446411133),
                  new google.maps.LatLng(1.4098842454741551, 103.853759765625),
                  new google.maps.LatLng(1.4028482491230558, 103.84517669677734),
                  new google.maps.LatLng(1.4021618093200738, 103.8424301147461),
                  new google.maps.LatLng(1.3970135043880962, 103.8372802734375),
                  new google.maps.LatLng(1.4013037592832867, 103.83419036865234),
                  new google.maps.LatLng(1.4061088354351594, 103.8369369506836),
                  new google.maps.LatLng(1.4030198590423297, 103.82835388183594),
                  new google.maps.LatLng(1.4085971745570094, 103.83007049560547),
                  new google.maps.LatLng(1.4097984407684854, 103.83513450622559),
                  new google.maps.LatLng(1.4091978077402003, 103.83891105651855),
                  new google.maps.LatLng(1.4073959077262157, 103.84285926818848),
                  new google.maps.LatLng(1.4085971745570094, 103.84603500366211),
                  new google.maps.LatLng(1.4102274642652444, 103.84740829467773),
                  new google.maps.LatLng(1.4175208515906825, 103.83333206176758),
                  new google.maps.LatLng(1.4040495182936055, 103.80998611450195),
                  new google.maps.LatLng(1.3673247271244882, 103.82698059082031),
                  new google.maps.LatLng(1.3611466692507197, 103.82766723632812),
                  new google.maps.LatLng(1.360803443348508, 103.82183074951172),
                  new google.maps.LatLng(1.3559982755948157, 103.81805419921875),
                  new google.maps.LatLng(1.3628627980286985, 103.81256103515625),
                  new google.maps.LatLng(1.360803443348508, 103.80191802978516),
                  new google.maps.LatLng(1.3400381858550037, 103.80517959594727),
                                  ];
   

                  var northEastCoords = [
                  new google.maps.LatLng(1.39443934768891, 103.88277053833008),
                  new google.maps.LatLng(1.3697273008963304, 103.87624740600586),
                  new google.maps.LatLng(1.3549685955482083, 103.87367248535156),
                  new google.maps.LatLng(1.3333452139746036, 103.88912200927734),
                  new google.maps.LatLng(1.3261373777548218, 103.90525817871094),
                  new google.maps.LatLng(1.3316290644037232, 103.9376163482666),
                  new google.maps.LatLng(1.335232977120653, 103.93332481384277),
                  new google.maps.LatLng(1.3393517280407568, 103.93555641174316),
                  new google.maps.LatLng(1.3409820650354305, 103.92053604125977),
                  new google.maps.LatLng(1.34484338516233, 103.92019271850586),
                  new google.maps.LatLng(1.3463879115035062, 103.92611503601074),
                  new google.maps.LatLng(1.3601169913975755, 103.96087646484375),
                  new google.maps.LatLng(1.3779646783713158, 103.97907257080078),
                  new google.maps.LatLng(1.3875749160752828, 103.97289276123047),
                  new google.maps.LatLng(1.3813969105879216, 103.96053314208984),
                  new google.maps.LatLng(1.3896342476555243, 103.93804550170898),
                  new google.maps.LatLng(1.402676639191187, 103.93169403076172),
                  new google.maps.LatLng(1.421038830212271, 103.91263961791992),
                  new google.maps.LatLng(1.4203523957796302, 103.90439987182617),
                  new google.maps.LatLng(1.417091829441639, 103.89890670776367),
                  new google.maps.LatLng(1.4081681507599295, 103.89427185058594),
                  new google.maps.LatLng(1.4030198590423297, 103.88774871826172),
                  new google.maps.LatLng(1.3954690107067005, 103.88534545898438),
                                  ];
                                
                                  

                  var SouthEastCoords = [
                  new google.maps.LatLng(1.2804872656134914, 103.875732421875),
                  new google.maps.LatLng(1.2872661877508906, 103.86929512023926),
                  new google.maps.LatLng(1.2955038410185278, 103.86611938476562),
                  new google.maps.LatLng(1.2986787627406342, 103.86684894561768),
                  new google.maps.LatLng(1.298550049775337, 103.87126922607422),
                  new google.maps.LatLng(1.3012101163916314, 103.87238502502441),
                  new google.maps.LatLng(1.3039130844347167, 103.87092590332031),
                  new google.maps.LatLng(1.3046853604856161, 103.8691234588623),
                  new google.maps.LatLng(1.3082893122529764, 103.86405944824219),
                  new google.maps.LatLng(1.3549685955482083, 103.85684967041016),
                  new google.maps.LatLng(1.3697273008963304, 103.86114120483398),
                  new google.maps.LatLng(1.3697273008963304, 103.875732421875),
                  new google.maps.LatLng(1.3553118222790563, 103.87350082397461),
                  new google.maps.LatLng(1.3336884437452605, 103.88877868652344),
                  new google.maps.LatLng(1.3261373777548218, 103.90560150146484),
                  new google.maps.LatLng(1.331457449380893, 103.93753051757812),
                  new google.maps.LatLng(1.334889747565498, 103.9335823059082),
                  new google.maps.LatLng(1.3393517280407568, 103.93568515777588),
                  new google.maps.LatLng(1.3398236678087188, 103.93283128738403),
                  new google.maps.LatLng(1.344628867537596, 103.92937660217285),
                  new google.maps.LatLng(1.3450579027681973, 103.92615795135498),
                  new google.maps.LatLng(1.346473718493781, 103.9262866973877),
                  new google.maps.LatLng(1.3600311848899818, 103.96096229553223),
                  new google.maps.LatLng(1.3780504842370611, 103.97872924804688),
                  new google.maps.LatLng(1.3868026662703206, 103.97435188293457),
                  new google.maps.LatLng(1.389376831306135, 103.97289276123047),
                  new google.maps.LatLng(1.3926374363241238, 103.97890090942383),
                  new google.maps.LatLng(1.3926374363241238, 103.98405075073242),
                  new google.maps.LatLng(1.3936671001299539, 103.9867115020752),
                  new google.maps.LatLng(1.3891194149286932, 103.99928569793701),
                  new google.maps.LatLng(1.3735027690977097, 104.00808334350586),
                  new google.maps.LatLng(1.3698989132164652, 104.00705337524414),
                  new google.maps.LatLng(1.3697273008963304, 104.01323318481445),
                  new google.maps.LatLng(1.3573711816421556, 104.03881072998047),
                  new google.maps.LatLng(1.3544537553607754, 104.04138565063477),
                  new google.maps.LatLng(1.357714408032226, 104.0324592590332),
                  new google.maps.LatLng(1.3537673016073588, 104.03228759765625),
                  new google.maps.LatLng(1.3496485750088296, 104.0346908569336),
                  new google.maps.LatLng(1.3479324368661145, 104.03228759765625),
                  new google.maps.LatLng(1.349133733693114, 104.03022766113281),
                  new google.maps.LatLng(1.3362626654984817, 104.02507781982422),
                  new google.maps.LatLng(1.3252793006139454, 104.02233123779297),
                  new google.maps.LatLng(1.3252793006139454, 104.03194427490234),
                  new google.maps.LatLng(1.316870128930104, 104.03366088867188),
                  new google.maps.LatLng(1.315668816369295, 104.02885437011719),
                  new google.maps.LatLng(1.3196159840368622, 104.02301788330078),
                  new google.maps.LatLng(1.3161836646805007, 104.02318954467773),
                  new google.maps.LatLng(1.3148107356145071, 104.01117324829102),
                  new google.maps.LatLng(1.3101770944467952, 104.00087356567383),
                  new google.maps.LatLng(1.3134378057934368, 103.99023056030273),
                  new google.maps.LatLng(1.3120648752180664, 103.98473739624023),
                  new google.maps.LatLng(1.3161836646805007, 103.98096084594727),
                  new google.maps.LatLng(1.3142958870200538, 103.96413803100586),
                  new google.maps.LatLng(1.2967909719264816, 103.90371322631836),
                  new google.maps.LatLng(1.2935302390231982, 103.89530181884766),
                                  ];

             
                                 

            //Construct the region polygon
            southWestBound_1 = new google.maps.Polygon({
              paths: southWestCoords_1,
              strokeColor: '#DB89EF',
              strokeOpacity: 0.8,
              strokeWeight: 2,
              fillColor: '#DB89EF',
              fillOpacity: 0.3, 
              editable:false
            });

            southWestBound_2 = new google.maps.Polygon({
              paths: southWestCoords_2,
              strokeColor: '#DB89EF',
              strokeOpacity: 0.8,
              strokeWeight: 3,
              fillColor: '#DB89EF',
              fillOpacity: 0.35
            });

            northWestBound = new google.maps.Polygon({
              paths: northWestCoords,
              strokeColor: '#A8DDAD',
              strokeOpacity: 0.8,
              strokeWeight: 3,
              fillColor: '#A8DDAD',
              fillOpacity: 0.35
            });

            centralSingaporeBound = new google.maps.Polygon({
              paths: centralSingaporeCoords,
              strokeColor: '#EAC97F',
              strokeOpacity: 0.8,
              strokeWeight: 3,
              fillColor: '#EAC97F',
              fillOpacity: 0.35
            });
            northEastBound = new google.maps.Polygon({
              paths: northEastCoords,
              strokeColor: '#FF7DB8',
              strokeOpacity: 0.8,
              strokeWeight: 3,
              fillColor: '#FF7DB8',
              fillOpacity: 0.35
            });

            SouthEastBound = new google.maps.Polygon({
              paths: SouthEastCoords,
              strokeColor: '#D4EFBF',
              strokeOpacity: 0.8,
              strokeWeight: 3,
              fillColor: '#D4EFBF',
              fillOpacity: 0.35
            });
                                  



        //Setting the region polygon on the map
        southWestBound_1.setMap(map);
        southWestBound_2.setMap(map);
        northWestBound.setMap(map);
        centralSingaporeBound.setMap(map);
        northEastBound.setMap(map);
        SouthEastBound.setMap(map);

	//Set markers on the map
	var image = "{% static "images/drop.png" %}";
  	var myLatlng = new google.maps.LatLng(1.377278, 103.797798);
  	marker = new google.maps.Marker({
    		map:map,
    		draggable:true,
    		animation: google.maps.Animation.DROP,
    		position: myLatlng,
		icon: image	
  	});
	{% for form in formList %}
		myLatlng = new google.maps.LatLng({{ form.X_coordinate }}, {{ form.Y_coordinate }});
  		marker = new google.maps.Marker({
    			map:map,
    			draggable:true,
    			animation: google.maps.Animation.DROP,
    			position: myLatlng,
			icon: image	
  		});
    	{% endfor %}
        //google.maps.event.addListener(marker, 'click', toggleBounce);

}

function toggleBounce() {

  if (marker.getAnimation() != null) {
    marker.setAnimation(null);
  } else {
    marker.setAnimation(google.maps.Animation.BOUNCE);
  }
}

google.maps.event.addDomListener(window, 'load', initialize);
