# faz ontologia, renderizando a figura, com os labels.
# ver OT, OPS, ORe
import percolation as P
import  importlib, datetime
importlib.reload(P.rdf)

tg=P.rdf.makeBasicGraph([["po","cm"],[P.rdf.ns.po,P.rdf.ns.cm]],"Conceitualização da caixa mágica")
tg2=P.rdf.makeBasicGraph([["po","cm"],[P.rdf.ns.po,P.rdf.ns.cm]],"Metadados da conceitualização da caixa mágica")
aname="MagicBox"
ind=P.rdf.IC([tg2],P.rdf.ns.po.Ontology,
        "MagicBox","Magic Box Ontology")
P.rdf.link([tg2],ind,"Magic Box Ontology",
                      [
                      P.rdf.ns.po.createdAt,
                      P.rdf.ns.po.availableAt,
                      P.rdf.ns.po.rdfFile,
                      P.rdf.ns.po.ttlFile,
                      P.rdf.ns.po.discorveryRDFFile,
                      P.rdf.ns.po.discoveryTTLFile,
                      P.rdf.ns.po.acquiredThrough,
                      P.rdf.ns.rdfs.comment,
                      ],
                      [
                       datetime.datetime.now(),
                       "https://github.com/ttm/caixamagica",
                       "https://raw.githubusercontent.com/ttm/{}/master/rdf/{}Translate.owl".format(aname,aname),
                       "https://raw.githubusercontent.com/ttm/{}/master/rdf/{}Translate.ttl".format(aname,aname),
                            "https://raw.githubusercontent.com/ttm/{}/master/rdf/{}Meta.owl".format(aname,aname),
                            "https://raw.githubusercontent.com/ttm/{}/master/rdf/{}Meta.ttl".format(aname,aname),
                       "Caixa Mágica group conceptualization at LabicBR (Nov/2015)",
                            "a high level (and still preliminary) conceptualization",
                       ])



P.rdf.C([tg],P.rdf.ns.cm.LegacyOfProcesses,
        "Legacy of Processes",None,
        "A generic collection of (participatory) processes validated through time, necessity or experts",u"Legado de Processos",
        "Uma coleção de processos (participativos) validados pelo tempo, necessidade ou especialistas",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.MagicBox,
        "Magic Box",P.rdf.ns.cm.LegacyOfProcesses,
        "The magic box of social participations",u"Caixa Mágica",
        "A caixa mágica de participação social",graph_lang="pt")

P.rdf.P([tg],P.rdf.ns.cm.component,"component","componente","a software or hardware component of a system")

P.rdf.L([tg],"Caixa Mágica","componente","Ágora Delibera")
P.rdf.L([tg],"Caixa Mágica","componente","Dialoga")
P.rdf.L([tg],"Caixa Mágica","componente","Participabr")


P.rdf.C([tg],P.rdf.ns.cm.Software,"Software",None,
        "Any software, from scripts to large systems",u"Software",
        "Qualquer software desde scripts a sistemas grandes")

P.rdf.C([tg],P.rdf.ns.cm.AgoraDelibera,"Ágora Delibera",P.rdf.ns.cm.Software,
        "A software for deliberation processes through phases","Ágora Delibera",
        "Um software para processos de deliberação através de fases")


P.rdf.C([tg],P.rdf.ns.cm.Dialoga,"Dialoga",P.rdf.ns.cm.Software,
        "A software for collecting opinions and proposals","Dialoga",
        "Um software para coletar opiniões e propostas")

P.rdf.C([tg],P.rdf.ns.cm.Participabr,"Participabr",P.rdf.ns.cm.Software,
        "A social participation software with many features","Participabr",
        "Um software de participação social com muitas ferramentas")

P.rdf.C([tg],P.rdf.ns.cm.Hardware,"Hardware",None,
        "Any hardware, from ICs to larger systems",u"Hardware",
        "Qualquer hardware desde CIs a sistemas maiores",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.ConnectiveHardware,"Connective Hardware",P.rdf.ns.cm.Hardware,
        "A hardware that performs communication with other hardware through dedicated protocols",u"Hardware Conectivo",
        "Um hardware que se comunica com outros hardware através de protocolos dedicados",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.LowCostHardware,"Low-Cost Hardware",P.rdf.ns.cm.Hardware,
        "A hardware with an accessible cost",u"Hardware de Baixo Custo",
        "Um hardware com custo reduzido",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.PortableHardware,"Portable Hardware",P.rdf.ns.cm.Hardware,
        "A hardware with ease of physical locality portability",
        "Hardware Portátil",
        "Um hardware com facilidade para portabilidade de localidade física",graph_lang="pt")

P.rdf.L([tg],"Caixa Mágica","componente","Hardware Conectivo")
P.rdf.L([tg],"Caixa Mágica","componente","Hardware de Baixo Custo")
P.rdf.L([tg],"Caixa Mágica","componente","Hardware Portátil")

P.rdf.C([tg],P.rdf.ns.cm.NonParticipant,"Non Participant",None,
        "A non-participant individual or group",
        "Não Participante",
        "Um indivíduo ou grupo não participante",
        graph_lang="pt")

P.rdf.P([tg],P.rdf.ns.cm.direction,"direction","direção","an overall direction of the initiative or some concept important for the group")
P.rdf.L([tg],"Caixa Mágica","direção","Não Participante")


P.rdf.P([tg],P.rdf.ns.cm.beneficiary,"beneficiary","beneficiário","the beneficiary of the initiative")
P.rdf.L([tg],"Caixa Mágica","beneficiário","Não Participante")

P.rdf.C([tg],P.rdf.ns.cm.NonIncluded,"Non Included",None,
        "A digitally or politically non-included individual or group",
        "Não Incluído",
        "Um indivíduo ou grupo não incluído digitalmente ou politicamente",
        graph_lang="pt")

P.rdf.L([tg],"Caixa Mágica","beneficiário","Não Incluído")

P.rdf.C([tg],P.rdf.ns.cm.Ourselves,"Ourselves",None,
        "We who are developing the Caixa Mágica project, participating at Labicbr (Nov/2015), and/or social participation interested individuals.",
        "Nós Mesmos",
        "Nós que estamos desenvolvendo o projeto da Caixa Mágica, participando do Labicbr (Nov/2015), e/ou indivíduos interessados em participação social",
        graph_lang="pt")

P.rdf.L([tg],"Caixa Mágica","beneficiário","Nós Mesmos")

P.rdf.P([tg],P.rdf.ns.cm.participationLevel,"participation level","nível de participação","the level of participation (5 levels on our standard conceptualization)")


P.rdf.C([tg],P.rdf.ns.cm.ParticipationLevel,
        "Participation Level",None,
        "The participation level of social participation: \
        1) Information, \
        2) Consultation, \
        3) Deliberation, \
        4) Joint Action, \
        5) Fostering Existing Initiatives.",
        "Nível de Participação",
        "O nível de participação social: \
        1) Informação, \
        2) Consulta, \
        3) Deliberação, \
        4) Ação Conjunta, \
        5) Fomento de Iniciativas Existentes.",graph_lang="pt")




P.rdf.C([tg],P.rdf.ns.cm.Deliberation,
        "Deliberation",P.rdf.ns.cm.ParticipationLevel,
        "The deliberation level of social participation.\
        This is the third level of social participation",
        "Deliberação",
        "O nível de deliberação de participação social.\
        Este é o terceiro nível de participação social.",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.Information,
        "Information",P.rdf.ns.cm.ParticipationLevel,
        "The information level of social participation.\
        This is the first level of social participation",
        "Informação",
        "O nível de informação de participação social.\
        Este é o primeiro nível de participação social.",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.Consultation,
        "Consultation",P.rdf.ns.cm.ParticipationLevel,
        "The consultation level of social participation.\
        This is the second level of social participation",
        "Consulta",
        "O nível de consulta de participação social.\
        Este é o segundo nível de participação social.",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.JointAction,
        "Joint Action",P.rdf.ns.cm.ParticipationLevel,
        "The joint action level of social participation.\
        This is the fourth level of social participation",
        "Ação Conjunta",
        "O nível de ação conjunta de participação social.\
        Este é o quarto nível de participação social.",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.FosteringExistingInitiatives,
        "Fostering Existing Initiatives",P.rdf.ns.cm.ParticipationLevel,
        "The 'fostering existing initiatives' level of social participation.\
        This is the fifth level of social participation",
        "Fomento de Iniciativas Existentes",
        "O nível de 'fomento de iniciativas existentes' de participação social.\
        Este é o quinto nível de participação social.",graph_lang="pt")

P.rdf.P([tg],P.rdf.ns.cm.participationLevel,"participation level","nível de participação","o nível de participação de um system ou processo participativo")
P.rdf.L([tg],"Caixa Mágica","nível de participação","Deliberação")

P.rdf.P([tg],P.rdf.ns.cm.level,"level","nível","uma referência numérica do nível de participação de um system, processo participativo ou conceito")
P.rdf.D([tg],P.rdf.ns.cm.Information,"nível",P.rdf.LL_(1))
P.rdf.D([tg],P.rdf.ns.cm.Consultation,"nível",P.rdf.LL_(2))
P.rdf.D([tg],P.rdf.ns.cm.Deliberation,"nível",P.rdf.LL_(3))
P.rdf.D([tg],P.rdf.ns.cm.JointAction,"nível",P.rdf.LL_(4))
P.rdf.D([tg],P.rdf.ns.cm.FosteringExistingInitiatives,"nível",P.rdf.LL_(5))

P.rdf.LD([tg],"Informação","nível",1)
P.rdf.LD([tg],"Consulta","nível",2)
P.rdf.LD([tg],"Deliberação","nível",3)
P.rdf.LD([tg],"Ação Conjunta","nível",4)
P.rdf.LD([tg],"Fomento de Iniciativas Existentes","nível",5)

P.rdf.C([tg],P.rdf.ns.cm.Empowerment,"Empowerment",None,
        "The empowerment of civil society individuals",
        "Empoderamento",
        "O empoderamento dos indivíduos da sociedade civil",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.SocialParticipation,"Social Participation",P.rdf.ns.cm.Empowerment,
        "The inclusion of the civil society in the governance of society",
        "Participação Social",
        "A inclusão da sociedade civil na governança da sociedade",graph_lang="pt")

P.rdf.C([tg],P.rdf.ns.cm.DigitalInclusion,"Digital Inclusion",P.rdf.ns.cm.Empowerment,
        "The inclusion of individuals in the use of digital technology",
        "Inclusão Digital",
        "A inclusão de indivíduos no uso de tecnologias digitais",graph_lang="pt")

P.rdf.P([tg],P.rdf.ns.cm.purpose,"purpose","propósito","the purpose of a system or concept")
P.rdf.L([tg],"Caixa Mágica","propósito","Inclusão Digital")
P.rdf.L([tg],"Caixa Mágica","propósito","Participação Social")





fpath_="../"
aname="caixaMagica"
P.rdf.writeAll(tg,aname+"Translate",fpath_,1)
P.rdf.writeAll(tg2,aname+"Meta",fpath_,1)
tg_=[tg[0]+tg2[0],tg[1]]
P.rdf.writeAll(tg_,aname+"Full",fpath_,1)
