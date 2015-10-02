# -*- coding: cp1252 -*-
from xml.dom.minidom import parse
import os, sys
import types
import MySQLdb
import datetime

def criarDicionario(xml):

    dic = {}

    for elemento in xml.childNodes:
        nome = str(elemento)[14:-14]
        listaFilhos = xml.getElementsByTagName(nome)            
        if len(listaFilhos) > 0:

            xmlValor = listaFilhos[0].toxml()

            if len(listaFilhos[0].childNodes) == 1 and xmlValor.count("<") == 2:
                        
                valor = xmlValor[len(nome) + 2:-(len(nome) + 3)]
                dic[nome] = valor

            else:
                dic[nome] = criarDicionario(listaFilhos[0])
                
        else:
            dic[nome] = criarDicionario(listaFilhos[0])
    return dic

def printarDicionario(dic, espaco):
    for chave, valor in dic.iteritems():
        if type (valor) is type(dic):
            print str(espaco) + str(chave) + ": "
            printarDicionario(valor, espaco + "     ")
        else:
            print espaco + chave + " = " + valor

def inserirNota(xmlNota):

    #####elementos do IDE #########
    #print "--------------elementos do IDE--------------"
    ide = xmlNota.getElementsByTagName("ide")[0]
    resultadoIDE = criarDicionario(ide)
    #printarDicionario(resultadoIDE, "")

    #print resultadoIDE

    #####elementos do EMIT #########
    #print "--------------elementos do EMIT--------------"
    emit = xmlNota.getElementsByTagName("emit")[0]
    resultadoEMIT = criarDicionario(emit)
    #printarDicionario(resultadoEMIT, "")

    #####elementos do DEST #########
    #print "--------------elementos do DEST--------------"
    dest = xmlNota.getElementsByTagName("dest")[0]
    resultadoDEST = criarDicionario(dest)
    #printarDicionario(resultadoDEST, "")

    #print resultadoDEST

    ####elementos dos ITEMS#########
    print "--------------elementos dos ITEMS --------------"
    items = {}
    resultadoDET = {}
    for i in range (0, len(xmlNota.getElementsByTagName("det"))):
        print "     ---- ITEM %i -------" % (i + 1)
        det = xmlNota.getElementsByTagName("det")[i]
        resultadoDET[i] = criarDicionario(det)
    #printarDicionario(resultadoDET, "     ")
    items["numero" + str(i + 1)] = resultadoDET

    #print resultadoDET

    #####elementos do TOTAL #########
    #print "--------------elementos do TOTAL--------------"
    total = xmlNota.getElementsByTagName("total")[0]
    resultadoTOTAL = criarDicionario(total)
    #printarDicionario(resultadoTOTAL, "")

    #print resultadoTOTAL

    #####elementos do TRANSP #########
    transp = xmlNota.getElementsByTagName("transp")    
    if len(transp) > 0:
        #print "--------------elementos da TRANSPORTADORA --------------"
        resultadoTRANSP = criarDicionario(transp[0])
        #printarDicionario(resultadoTRANSP, "")

    #print resultadoTRANSP

    ###elementos da COBR #########
    cobr = xmlNota.getElementsByTagName("cobr")
    if len(cobr) > 0:
        #print "--------------elementos da COBR --------------"
        resultadoCOBR = criarDicionario(cobr[0])
        #printarDicionario(resultadoCOBR, "")
        #print resultadoCOBR

    lista = ['ACA/ACC', 'AH', 'AH/H/V', 'AM', 'AM0/4ML', 'AM0/5ML', 'AM1/5ML', 'AM10ML', 'AM1ML', 'AM2/5ML', 'AM2ML', 'AM3ML', 'AM4ML', 'AM5ML', 'AM6ML', 'AM7ML', 'ANO', 'ANOS', 'ARR',
             'AWG', 'BAR', 'BAR.', 'BD', 'BIS', 'BIS/GL', 'BIS1/65G',
             'BIS1/8G', 'BIS100G', 'BIS10G', 'BIS135G', 'BIS13G',
             'BIS14G', 'BIS15G', 'BIS1G', 'BIS20G', 'BIS25G',
             'BIS28/8G', 'BIS28G', 'BIS2G', 'BIS3/5G', 'BIS30G',
             'BIS30ML', 'BIS40G', 'BIS43G', 'BIS45G', 'BIS47G', 'BIS4G',
             'BIS50G', 'BIS55G', 'BIS56G', 'BIS5G', 'BIS60G', 'BIS6G',
             'BIS7/5G', 'BIS70G', 'BIS80G', 'BIS90G', 'BIT', 'BL',
             'BLIS', 'BLIS21CP', 'BLIS35CP', 'BOB', 'BOL', 'BOM', 'BPM',
             'BPS', 'BR', 'BRI', 'BTJ', 'BTU', 'BTU/H', 'BWG', 'C',
             'CA', 'CAD',  'CAL/G', 'CAPS', 'CAR', 'CC', 'CD', 'CD/M2',
             'CG', 'CH', 'CIL', 'CIN', 'CJ', 'CL', 'CM', 'CM/POL',
             'CM2', 'CM2/H', 'CM2/M', 'CM3', 'CM\xb3/H', 'CM\xb3/MIN',
             'CNT', 'CO',  'COL', 'COMP', 'COMPR', 'C\xd3PIA', 'COPO',
             'CP', 'CPL', 'CPM', 'CPS', 'CRT', 'CS', 'CST', 'CT', 'CTE',
             'CV', 'CX', 'CX100UN', 'CX40UN', 'D', 'DAG', 'DAL', 'DAM',
             'DAN', 'DB', 'DBM', 'DG', 'DGT', 'DIA', 'DIAS', 'DL',
             'DM', 'DM2', 'DM3', 'DOSE(S)', 'DPI', 'DPT', 'DRAG', 'DZ',
             'EMB', 'EMB/H', 'ENV', 'ENV27/9G', 'ENV30G', 'EQP', 'F',
             'FCK',  'FD', 'FL', 'FLAC', 'FLS/H', 'FPS', 'FR',
             'FR1000ML', 'FR100DS', 'FR100ML', 'FR105ML', 'FR10ML',
             'FR110ML', 'FR1200MG', 'FR120DS', 'FR120ML', 'FR125ML',
             'FR130DS',  'FR1500MG', 'FR150DS', 'FR150ML', 'FR15ML',
             'FR160ML', 'FR200DS', 'FR200ML', 'FR20ML', 'FR240ML',
             'FR250ML', 'FR300DS', 'FR300ML', 'FR30DS', 'FR30G',
             'FR30ML', 'FR340ML',  'FR350ML', 'FR40ML', 'FR45ML',
             'FR500ML', 'FR50ML', 'FR600MG', 'FR60DS', 'FR60ML',
             'FR70ML', 'FR75ML', 'FR80ML', 'FR900MG', 'FR90ML', 'FR-AM',
             'FRENCH', 'FT', 'G', 'G/CM2', 'G/CM3', 'G/G', 'G/KG',
             'G/L', 'G/M', 'G/M2', 'G/M3', 'G/ML', 'G/MOL', 'GAU', 'GB',
             'GB/S', 'GBQ/ML', 'GHZ', 'GL', 'GL/H', 'GLOB', 'GR', 'GRA',
             'GRAN', 'GRF', 'GRR', 'H', 'HA', 'HENRY', 'HG', 'HL',
             'HM', 'HP', 'HZ', 'IPM', 'J', 'JD', 'JD2', 'JG', 'K', 'KA',
             'KA/S', 'KA/VCA', 'KB', 'KB/S', 'KBIT/S', 'KBPS', 'KCAL',
             'KCAL/G', 'KCAL/KG', 'KDA', 'KG', 'KG.CM', 'KG/CM2',
             'KG/DIA', 'KG/H', 'KG/KM', 'KG/L', 'KG/M', 'KG/M2',
             'KG/M3', 'KG/MM2', 'KGF', 'KGF/CM2', 'KGF/M2', 'KGF/MM2',
             'KHZ', 'KHZ-MHZ', 'KLT', 'KM', 'KM/H', 'KM/L', 'KN',
             'KN/M2', 'KOHM', 'KPA', 'KPB', 'KUI', 'KV', 'KV/MM', 'KVA',
             'KVA/KW', 'KVAR', 'KW', 'KW/H', 'L', 'L/H', 'L/M/H',
             'L/MIN', 'L/S', 'LB', 'LB.P\xc9', 'LB.POL', 'LB/POL2',
             'LM', 'LOG', 'LOTE', 'LPI', 'LT', 'LX', 'M', 'M/GRAU',
             'M/H', 'M/M', 'M/MIN', 'M/S', 'M2', 'M2/GL', 'M2/H',
             'M2/KG', 'M2/L', 'M3', 'M3/H', 'M3/KG', 'M3/MIN', 'M3/S',
             'MA', 'MAH', 'MB', 'MB/H', 'MB/S', 'MBAR.', 'MBPS', 'MBQ',
             'MBQ/ML', 'M\xc7', 'MCA', 'MCAL/KG', 'MCD', 'MCG', 'MCG/G',
             'MCG/ML', 'MCI', 'MCI', 'MCI/KG', 'MCI/ML', 'MCL', 'MCM',
             'MCU', 'MEQ/ML', 'M\xcaS', 'MESES', 'MESH', 'MF', 'MG',
             'MG/DL', 'MG/G', 'MG/KG', 'MG/L', 'MG/ML', 'MG/MOL', 'MGW',
             'MH', 'MHZ', 'MI', 'MICRA', 'MICROA', 'MICROF', 'MICROG',
             'MICROL', 'M\xcdCRON', 'MIL', 'MIL CTE', 'MIL UI', 'MIN',
             'MIW/CM\xb2', 'MKGF', 'ML', 'ML/L', 'ML/MIN', 'ML/MM',
             'ML/S', 'MM', 'MM/MIN', 'MM/S', 'MM2', 'MM3', 'MMCA',
             'MMHG', 'MMOL/KG', 'MN', 'MOHM', 'MOL', 'MPA', 'MPA/S',
             'MPX', 'MS', 'MS/L', 'MUI', 'MV', 'MVA', 'MVAR', 'MW', 'N',
             'N M', 'N/MM', 'N/MM\xb2', 'NA/S', 'NF', 'NM', 'NS', 'NTU',
             'OCT', 'OHM', 'OHM/KM', 'OHMS', 'OUTR', 'OUTRAS', 'OZ',
             'OZ.IN', 'P', 'PAL', 'PAR', 'PAST', 'PB', 'PC', 'PCT',
             'PCT100UN', 'PCT10UN', 'PCT500UN', 'PE', 'PER', 'PF',
             'PF/FT', 'PF/M', 'PH', 'POL', 'POL.HG', 'POL/S', 'POL\xb2',
             'POTE', 'POTE200G', 'POTE30G', 'POTE400G', 'POTE40G',
             'PPM', 'PPP', 'PPS', 'PR', 'PSI', 'PSIG', 'PX', 'RA', 'RC',
             'RES', 'RO', 'RPM', 'S', 'SAC', 'SAC100MG', 'SAC150MG',
             'SAC200MG', 'SAC300MG', 'SC', 'SER', 'SER-02G', 'SER-O',
             'SF', 'SUP', 'T', 'T/H', 'T/M\xb2', 'T/M3', 'TAB', 'TB',
             'TBO', 'TBTE', 'TESTE', 'TF', 'TR', 'U/G', 'U/MG', 'UFC',
             'UI', 'UI/G', 'UI/L', 'UI/ML', 'UN', 'UN/CM\xb2', 'UN/H',
             'UN/KG', 'UN/M2', 'UN/MCL', 'UN/MIN', 'US', 'UTR', 'V',
             'V/HZ', 'V/V', 'VA', 'VAR', 'VCA', 'VCA/VCC', 'VCC', 'VDC',
             'VRMS', 'W', 'W/H', 'WRMS', 'X']

    ##### Variaveis de Emitente #####
    
    if (resultadoEMIT.has_key('xNome')): nomeEmit = str(resultadoEMIT['xNome']).upper()
    else: nomeEmit = None
    
    if (resultadoEMIT.has_key('xFant')): nome_fantasiaEmit = str(resultadoEMIT['xFant']).upper()
    else: nome_fantasiaEmit = None
    
    if (resultadoEMIT.has_key('CNPJ')): cnpjEmit = str(resultadoEMIT['CNPJ']).upper()
    else: cnpjEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('xLgr')): logradouroEmit = str(resultadoEMIT['enderEmit']['xLgr']).upper()
    else: logradouroEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('nro')): numeroEmit = str(resultadoEMIT['enderEmit']['nro']).upper()
    else: numeroEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('xCpl')): complementoEmit = str(resultadoEMIT['enderEmit']['xCpl']).upper()
    else: complementoEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('xMun')): municipioEmit = str(resultadoEMIT['enderEmit']['xMun']).upper()
    else: municipioEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('cMun')): cod_municipioEmit = str(resultadoEMIT['enderEmit']['cMun']).upper()
    else: cod_municipioEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('xBairro')): bairroEmit = str(resultadoEMIT['enderEmit']['xBairro']).upper()
    else: bairroEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('UF')): ufEmit = str(resultadoEMIT['enderEmit']['UF']).upper()
    else: ufEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('xPais')): paisEmit = str(resultadoEMIT['enderEmit']['xPais']).upper()
    else: paisEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('cPais')): cod_paisEmit = str(resultadoEMIT['enderEmit']['cPais']).upper()
    else: cod_paisEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('CEP')): cepEmit = str(resultadoEMIT['enderEmit']['CEP']).upper()
    else: cepEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('fone')): foneEmit = str(resultadoEMIT['enderEmit']['fone']).upper()
    else: foneEmit = None
    
    if (resultadoEMIT.has_key('CRT')): crtEmit = str(resultadoEMIT['CRT']).upper()
    else: crtEmit = None
    
    if (resultadoEMIT.has_key('IM')): imEmit = str(resultadoEMIT['IM']).upper()
    else: imEmit = None
    
    if (resultadoEMIT.has_key('IE')): ieEmit = str(resultadoEMIT['IE']).upper()
    else: ieEmit = None
    
    if (resultadoEMIT.has_key('CNAE')): cnaeEmit = str(resultadoEMIT['CNAE']).upper()
    else: cnaeEmit = None
    
    if (resultadoEMIT['enderEmit'].has_key('cMun')): municipio_icmsEmit = str(resultadoEMIT['enderEmit']['cMun']).upper()
    else: municipio_icmsEmit = None
    
    if (resultadoEMIT.has_key('IEST')): ie_tributarioEmit = str(resultadoEMIT['IEST']).upper()
    else: ie_tributarioEmit = None

    ##### Variaveis de Destinatario #####

    if (resultadoDEST.has_key('xNome')): nomeDest = str(resultadoDEST['xNome']).upper()
    else: nomeDest = None
    
    if (resultadoDEST.has_key('CNPJ')): cnpjDest = str(resultadoDEST['CNPJ']).upper()
    else: cnpjDest = None
    
    if (resultadoDEST.has_key('CPF')): cpfDest = str(resultadoDEST['CPF']).upper()
    else: cpfDest = None
    
    if (resultadoDEST['enderDest'].has_key('xLgr')): logradouroDest = str(resultadoDEST['enderDest']['xLgr']).upper()
    else: logradouroDest = None
    
    if (resultadoDEST['enderDest'].has_key('nro')): numeroDest = str(resultadoDEST['enderDest']['nro']).upper()
    else: numeroDest = None
    
    if (resultadoDEST['enderDest'].has_key('xMun')): municipioDest = str(resultadoDEST['enderDest']['xMun']).upper()
    else: municipioDest = None
    
    if (resultadoDEST['enderDest'].has_key('cMun')): cod_municipioDest = str(resultadoDEST['enderDest']['cMun']).upper()
    else: cod_municipioDest = None
    
    if (resultadoDEST['enderDest'].has_key('xBairro')): bairroDest = str(resultadoDEST['enderDest']['xBairro']).upper()
    else: bairroDest = None
    
    if (resultadoDEST['enderDest'].has_key('UF')): ufDest = str(resultadoDEST['enderDest']['UF']).upper()
    else: ufDest = None
    
    if (resultadoDEST['enderDest'].has_key('xPais')): paisDest = str(resultadoDEST['enderDest']['xPais']).upper()
    else: paisDest = None
    
    if (resultadoDEST['enderDest'].has_key('cPais')): cod_paisDest = str(resultadoDEST['enderDest']['cPais']).upper()
    else: cod_paisDest = None
    
    if (resultadoDEST['enderDest'].has_key('CEP')): cepDest = str(resultadoDEST['enderDest']['CEP']).upper()
    else: cepDest = None
    
    if (resultadoDEST['enderDest'].has_key('fone')): foneDest = str(resultadoDEST['enderDest']['fone']).upper()
    else: foneDest = None
    
    if (resultadoDEST.has_key('email')): emailDest = str(resultadoDEST['email']).upper()
    else: emailDest = None
    
    if (resultadoDEST.has_key('IE')): ieDest = str(resultadoDEST['IE']).upper()
    else: ieDest = None
    
    insc_suframaDest = None
    indicador_ieDest = None
    imDest = None

    #####Variaveis de Transporte #####

    if (resultadoTRANSP.has_key('modFrete')): mod_freteTransp = str(resultadoTRANSP['modFrete']).upper()
    else: mod_freteTransp = None
    
    if (resultadoTRANSP.has_key('transporta')):
        
        if (resultadoTRANSP['transporta'].has_key('xNome')): nomeTransp = str(resultadoTRANSP['transporta']['xNome']).upper()
        else: nomeTransp = None

        if (resultadoTRANSP['transporta'].has_key('CNPJ')): cnpjTransp = str(resultadoTRANSP['transporta']['CNPJ']).upper()
        else: cnpjTransp = None
        
        if (resultadoTRANSP['transporta'].has_key('xEnder')): enderecoTransp = str(resultadoTRANSP['transporta']['xEnder']).upper()
        else: enderecoTransp = None
        
        if (resultadoTRANSP['transporta'].has_key('xMun')): municipioTransp = str(resultadoTRANSP['transporta']['xMun']).upper()
        else: municipioTransp = None
        
        if (resultadoTRANSP['transporta'].has_key('UF')): ufTransp = str(resultadoTRANSP['transporta']['UF']).upper()
        else: ufTransp = None
        
        if (resultadoTRANSP['transporta'].has_key('IE')): ieTransp = str(resultadoTRANSP['transporta']['IE']).upper()
        else: ieTransp = None
        
    else:
        nomeTransp = None
        cnpjTransp = None
        enderecoTransp = None
        municipioTransp = None
        ufTransp = None
        ieTransp = None
        
    if (resultadoTRANSP.has_key('veicTransp')):
        
        if (resultadoTRANSP['veicTransp'].has_key('placa')): veiculoTransp = str(resultadoTRANSP['veicTransp']['placa']).upper()
        else: veiculoTransp = None
        
        if (resultadoTRANSP['veicTransp'].has_key('UF')): uf_veiculoTransp = str(resultadoTRANSP['veicTransp']['UF']).upper()
        else: uf_veiculoTransp = None
        
        if (resultadoTRANSP['veicTransp'].has_key('RNTC')): rntcTransp = str(resultadoTRANSP['veicTransp']['RNTC']).upper()
        else: rntcTransp = None
        
    else:
        veiculoTransp = None
        uf_veiculoTransp = None
        rntcTransp = None

    ##### Variaveis de Totais #####

    if (resultadoTOTAL['ICMSTot'].has_key('vBC')): bc_icmsTot = float(resultadoTOTAL['ICMSTot']['vBC'])
    else: bc_icmsTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vICMS')): icmsTot = float(resultadoTOTAL['ICMSTot']['vICMS'])
    else: icmsTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vBCST')): bc_icms_stTot = float(resultadoTOTAL['ICMSTot']['vBCST'])
    else: bc_icms_stTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vST')): icms_substituicaoTot = float(resultadoTOTAL['ICMSTot']['vST'])
    else: icms_substituicaoTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vProd')): produtosTot = float(resultadoTOTAL['ICMSTot']['vProd'])
    else: produtosTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vFrete')): freteTot = float(resultadoTOTAL['ICMSTot']['vFrete'])
    else: freteTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vSeg')): seguroTot = float(resultadoTOTAL['ICMSTot']['vSeg'])
    else: seguroTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vOutro')): outras_despesasTot = float(resultadoTOTAL['ICMSTot']['vOutro'])
    else: outras_despesasTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vIPI')): ipiTot = float(resultadoTOTAL['ICMSTot']['vIPI'])
    else: ipiTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vNF')): nfeTot = float(resultadoTOTAL['ICMSTot']['vNF'])
    else: nfeTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vDesc')): descontosTot = float(resultadoTOTAL['ICMSTot']['vDesc'])
    else: descontosTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vII')): iiTot = float(resultadoTOTAL['ICMSTot']['vII'])
    else: iiTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vPIS')): pisTot = float(resultadoTOTAL['ICMSTot']['vPIS'])
    else: pisTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vCOFINS')): cofinsTot = float(resultadoTOTAL['ICMSTot']['vCOFINS'])
    else: cofinsTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vCOFINS')): cofinsTot = float(resultadoTOTAL['ICMSTot']['vCOFINS'])
    else: cofinsTot = None
    
    if (resultadoTOTAL['ICMSTot'].has_key('vTotTrib')): aprox_tributosTot = float(resultadoTOTAL['ICMSTot']['vTotTrib'])
    else: aprox_tributosTot = None
    
    icms_desoneradoTot = None

    ##### Variaveis de Volume #####

    if (resultadoTRANSP.has_key('vol')):
        
        if (resultadoTRANSP['vol'].has_key('qVol')): quantidadeVol = str(resultadoTRANSP['vol']['qVol']).upper()
        else: quantidadeVol = None
        
        if (resultadoTRANSP['vol'].has_key('esp')): especieVol = str(resultadoTRANSP['vol']['esp']).upper()
        else: especieVol = None
        
        if (resultadoTRANSP['vol'].has_key('marca')): marca_volumeVol = str(resultadoTRANSP['vol']['marca']).upper()
        else: marca_volumeVol = None
        
        if (resultadoTRANSP['vol'].has_key('pesoL')): peso_liquidoVol = str(resultadoTRANSP['vol']['pesoL']).upper()
        else: peso_liquidoVol = None
        
        if (resultadoTRANSP['vol'].has_key('pesoB')): peso_brutoVol = str(resultadoTRANSP['vol']['pesoB']).upper()
        else: peso_brutoVol = None
        
    else:
        quantidadeVol = None
        especieVol = None
        marca_volumeVol = None
        peso_liquidoVol = None
        peso_brutoVol = None
        
    numeracaoVol = None

    ##### Variaveis de Nfe #####

    if (resultadoIDE.has_key('mod')): modeloNfe = str(resultadoIDE['mod']).upper()
    else: modeloNfe = None
    
    if (resultadoIDE.has_key('serie')): serieNfe = str(resultadoIDE['serie']).upper()
    else: serieNfe = None
    
    if (resultadoIDE.has_key('nNF')): numeroNfe = str(resultadoIDE['nNF']).upper()
    else: numeroNfe = None
    
    if (resultadoIDE.has_key('dEmi')): data_emissaoNfe = str(resultadoIDE['dEmi']).upper()
    else: data_emissaoNfe = None
    
    if (resultadoIDE.has_key('dSaiEnt')): data_saiEntNfe = str(resultadoIDE['dSaiEnt']).upper()
    else: data_saiEntNfe = None
    
    if (resultadoIDE.has_key('hSaiEnt')): hora_saiEntNfe = str(resultadoIDE['hSaiEnt']).upper()
    else: hora_saiEntNfe = None
    
    valor_nfNfe = nfeTot
    
    if (resultadoIDE.has_key('procEmi')): processoNfe = str(resultadoIDE['procEmi']).upper()
    else: processoNfe = None
    
    if (resultadoIDE.has_key('verProc')): versao_processoNfe = str(resultadoIDE['verProc']).upper()
    else: versao_processoNfe = None
    
    if (resultadoIDE.has_key('tpEmis')): tipo_emissaoNfe = str(resultadoIDE['tpEmis']).upper()
    else: tipo_emissaoNfe = None
    
    if (resultadoIDE.has_key('finNFe')): finalidadeNfe = str(resultadoIDE['finNFe']).upper()
    else: finalidadeNfe = None
    
    if (resultadoIDE.has_key('natOp')): natureza_operacaoNfe = str(resultadoIDE['natOp']).upper()
    else: natureza_operacaoNfe = None
    
    if (resultadoIDE.has_key('indPag')): tipo_pagamentoNfe = str(resultadoIDE['indPag']).upper()
    else: tipo_pagamentoNfe = None
    
    chaveNfe = None
    versao_xmlNfe = None
    tipo_operacaoNfe = None
    digest_nfeNfe = None
    
    ##### Abrir Conexao #####

    con = MySQLdb.connect(host='localhost', user='root', passwd='', db='nfe2')
    c = con.cursor()
    d = con.cursor()
    e = con.cursor()
    f = con.cursor()
    g = con.cursor()
    h = con.cursor()
    i = con.cursor()
    j = con.cursor()
    k = con.cursor()
    l = con.cursor()
    m = con.cursor()
    n = con.cursor()

    try:

        ##### Insert do Emitente #####
        print "Chegou aqui 1"
        
        verifEmit = c.execute("SELECT id FROM emitente WHERE cnpj='%s'" % (cnpjEmit))
            
        if (verifEmit == 0):
            c.execute("INSERT INTO emitente VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (nomeEmit, nome_fantasiaEmit, cnpjEmit, logradouroEmit, numeroEmit, complementoEmit, municipioEmit, cod_municipioEmit, municipio_icmsEmit, bairroEmit, ufEmit, paisEmit, cod_paisEmit, cepEmit, foneEmit, crtEmit, imEmit, ieEmit, ie_tributarioEmit, cnaeEmit))
            idEmit = c.lastrowid
            print "Chegou aqui 2"
        else:
            listagem = c.fetchall()
            idEmit = long(listagem[0][0])
            print "Chegou aqui 3"

        ##### Insert do Destinatario #####
        

        if (cpfDest == None):
            verifDest = d.execute("SELECT id FROM destinatario WHERE cnpj='%s'" % (cnpjDest))
        elif (cnpjDest == None):
            verifDest = d.execute("SELECT id FROM destinatario WHERE cpf='%s'" % (cpfDest))

        if (verifDest == 0):
            d.execute("INSERT INTO destinatario VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (nomeDest, cnpjDest, cpfDest, logradouroDest, numeroDest, municipioDest, cod_municipioDest, bairroDest, ufDest, paisDest, cod_paisDest, cepDest, foneDest, emailDest, insc_suframaDest, ieDest, indicador_ieDest, imDest))
            idDest = d.lastrowid
        else:
            listagem = d.fetchall()
            idDest = long(listagem[0][0])

        ##### Insert do Transporte #####

        verifTransp = e.execute("SELECT id FROM transporte WHERE mod_frete='%s' AND cnpj='%s'" % (mod_freteTransp, cnpjTransp))

        if (verifTransp == 0):
            e.execute("INSERT INTO transporte VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (mod_freteTransp, nomeTransp, cnpjTransp, enderecoTransp, municipioTransp, ufTransp, ieTransp, veiculoTransp, uf_veiculoTransp, rntcTransp))
            idTransp = e.lastrowid
        else:
            listagem = e.fetchall()
            idTransp = long(listagem[0][0])

        ##### Insert de Totais #####

        f.execute("INSERT INTO totais VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (bc_icmsTot, icmsTot, icms_desoneradoTot, bc_icms_stTot, icms_substituicaoTot, produtosTot, freteTot, seguroTot, outras_despesasTot, ipiTot, nfeTot, descontosTot, iiTot, pisTot, cofinsTot, aprox_tributosTot))    
        idTot = f.lastrowid
        
        ##### Insert de Volume #####

        g.execute("INSERT INTO volume VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)" , (idTransp, quantidadeVol, especieVol, marca_volumeVol, numeracaoVol, peso_liquidoVol, peso_brutoVol))
        idVol = g.lastrowid

        ##### Insert de Nfe #####

        h.execute("INSERT INTO nfe VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (idEmit, idDest, idTransp, idTot, chaveNfe, modeloNfe, serieNfe, numeroNfe, data_emissaoNfe, data_saiEntNfe, hora_saiEntNfe, valor_nfNfe, versao_xmlNfe, processoNfe, versao_processoNfe, tipo_emissaoNfe, finalidadeNfe, natureza_operacaoNfe, tipo_operacaoNfe, tipo_pagamentoNfe, digest_nfeNfe))
        idNfe = h.lastrowid

        ##### Loop #####

        for item in range(0, len(resultadoDET)):

            ##### Variaveis auxiliares #####
            
            if (resultadoDET[item]['imposto']['ICMS'].has_key('ICMS00')): icmsVar = 'ICMS00'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMS10')): icmsVar = 'ICMS10'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMS20')): icmsVar = 'ICMS20'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMS40')): icmsVar = 'ICMS40'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMS60')): icmsVar = 'ICMS60'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMS90')): icmsVar = 'ICMS90'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMSSN101')): icmsVar = 'ICMSSN101'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMSSN102')): icmsVar = 'ICMSSN102'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMSSN201')): icmsVar = 'ICMSSN201'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMSSN202')): icmsVar = 'ICMSSN202'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMSSN500')): icmsVar = 'ICMSSN500'
            elif (resultadoDET[item]['imposto']['ICMS'].has_key('ICMSSN900')): icmsVar = 'ICMSSN900'
            else: icmsVar = None
            
            if (resultadoDET[item]['imposto']['PIS'].has_key('PISNT')): pisVar = 'PISNT'
            elif (resultadoDET[item]['imposto']['PIS'].has_key('PISAliq')): pisVar = 'PISAliq'
            elif (resultadoDET[item]['imposto']['PIS'].has_key('PISOutr')): pisVar = 'PISOutr'
            else: pisVar = None

            if (resultadoDET[item]['imposto']['COFINS'].has_key('COFINSNT')): cofinsVar = 'COFINSNT'
            elif (resultadoDET[item]['imposto']['COFINS'].has_key('COFINSAliq')): cofinsVar = 'COFINSAliq'
            elif (resultadoDET[item]['imposto']['COFINS'].has_key('COFINSOutr')): cofinsVar = 'COFINSOutr'
            else: cofinsVar = None

            ##### Variaveis de Tipo de Produto #####
            
            if (resultadoDET[item]['prod'].has_key('NCM')):
                ncmTProd = str(resultadoDET[item]['prod']['NCM']).upper()
            else: ncmTProd = None

            ##### Variaveis de Produto #####
                
            if (resultadoDET[item]['prod'].has_key('xProd')):
                produtoProd = str(resultadoDET[item]['prod']['xProd'].encode('latin-1')).upper()
            else: produtoProd = None
            if '&quot;' in produtoProd:
                produtoProd = produtoProd.replace('&quot;','')
            
            if (resultadoDET[item]['prod'].has_key('cProd')): cod_produtoProd = str(resultadoDET[item]['prod']['cProd']).upper()
            else: cod_produtoProd = None

            ##### Variaveis de Item NF #####

            if (resultadoDET[item]['prod'].has_key('qCom')): quantidadeINF = resultadoDET[item]['prod']['qCom']
            else: quantidadeINF = None
            
            if (resultadoDET[item]['prod'].has_key('uCom')):
                unid_comercialINF = str(resultadoDET[item]['prod']['uCom']).upper()
                if not(unid_comercialINF in lista):
                    unid_comercialINF = 'UN'
            else:
                unid_comercialINF = None

            if (resultadoDET[item]['prod'].has_key('uTrib')):
                unid_tributavelINF = str(resultadoDET[item]['prod']['uTrib']).upper()
                if not(unid_tributavelINF in lista):
                    unid_tributavelINF = 'UN'
            else:
                unid_tributavelINF = None
            
            if (resultadoDET[item]['prod'].has_key('vProd')): valorINF = float(resultadoDET[item]['prod']['vProd'])
            else: valorINF = None
            
            if (resultadoDET[item]['prod'].has_key('CFOP')): cfopINF = str(resultadoDET[item]['prod']['CFOP']).upper()
            else: cfopINF = None
            
            if (resultadoDET[item]['prod'].has_key('indTot')): indicador_comp_nfeINF = str(resultadoDET[item]['prod']['indTot']).upper()
            else: indicador_comp_nfeINF = None
            
            if (resultadoDET[item]['prod'].has_key('qTrib')): quant_tributavelINF = resultadoDET[item]['prod']['qTrib']
            else: quant_tributavelINF = None
            
            if (resultadoDET[item]['prod'].has_key('vUnTrib')):
                valor_unitario_tribINF = float(resultadoDET[item]['prod']['vUnTrib'])
                valor_unitario_tribINF = round(valor_unitario_tribINF, 2)
            else:
                valor_unitario_tribINF = None
            if (resultadoDET[item]['prod'].has_key('vUnCom')):
                valor_unitario_comINF = float(resultadoDET[item]['prod']['vUnCom'])
                valor_unitario_comINF = round(valor_unitario_comINF, 2)
                
            else:
                valor_unitario_comINF = None
                
            if (resultadoDET[item]['prod'].has_key('xPed')): numero_pedidoINF = str(resultadoDET[item]['prod']['xPed']).upper()
            else: numero_pedidoINF = None
            
            if (resultadoDET[item]['prod'].has_key('nItemPed')): item_pedidoINF = str(resultadoDET[item]['prod']['nItemPed']).upper()
            else: item_pedidoINF = None
            
            if (resultadoDET[item]['prod'].has_key('nFCI')): fciINF = str(resultadoDET[item]['prod']['nFCI']).upper()
            else: fciINF = None
            
            if (resultadoDET[item]['prod'].has_key('vDesc')): descontoINF = str(resultadoDET[item]['prod']['vDesc']).upper()
            else: descontoINF = None
            
            if (resultadoDET[item]['prod'].has_key('cEAN') and resultadoDET[item]['prod']['cEAN']<>{}): cod_ean_comercialINF = str(resultadoDET[item]['prod']['cEAN']).upper()
            else: cod_ean_comercialINF = None
            
            if (resultadoDET[item]['prod'].has_key('cEANTrib') and resultadoDET[item]['prod']['cEANTrib']<>{}): cod_ean_tributavelINF = str(resultadoDET[item]['prod']['cEANTrib']).upper()
            else: cod_ean_tributavelINF = None
            
            if (resultadoDET[item]['imposto'].has_key('vTotTrib')): valor_aprox_tributosINF = str(resultadoDET[item]['imposto']['vTotTrib']).upper()
            else: valor_aprox_tributosINF = None
                
            cod_exp_tipiINF = None
            outras_despesasINF = None
            freteINF = None
            seguroINF = None

            ##### Variavel de Tipo de Imposto #####

            nomeTImp = " "

            ##### Variaveis de Imposto #####

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('CST')): icms_cstImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['CST']
            else: icms_cstImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('orig')): icms_origemImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['orig']
            else: icms_origemImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('pCredSN')): icms_alicota_aplic_calc_credImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['pCredSN']
            else: icms_alicota_aplic_calc_credImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('vCredICMSSN')): icms_valor_cred_aprovImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['vCredICMSSN']
            else: icms_valor_cred_aprovImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('modBC')): icms_mod_det_base_calcImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['modBC']
            else: icms_mod_det_base_calcImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('vBC')): icms_valor_base_calcImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['vBC']
            else: icms_valor_base_calcImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('pICMS')): icms_aliquotaImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['pICMS']
            else: icms_aliquotaImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('vICMS')): icms_valorImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['vICMS']
            else: icms_valorImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('modBCST')): icms_st_mod_BC_ICMS_STImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['modBCST']
            else: icms_st_mod_BC_ICMS_STImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('vBCST')): icms_st_base_calcImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['vBCST']
            else: icms_st_base_calcImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('pICMSST')): icms_st_aliquotaImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['pICMSST']
            else: icms_st_aliquotaImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('vICMSST')): icms_st_valorImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['vICMSST']
            else: icms_st_valorImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('vBCSTRet')): icms_st_base_calc_retido_anteriormenteImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['vBCSTRet']
            else: icms_st_base_calc_retido_anteriormenteImp = None

            if (resultadoDET[item]['imposto']['ICMS'][icmsVar].has_key('vICMSSTRet')): icms_st_valor_retido_anteriormenteImp = resultadoDET[item]['imposto']['ICMS'][icmsVar]['vICMSSTRet']
            else: icms_st_valor_retido_anteriormenteImp = None

            if (resultadoDET[item]['imposto'].has_key('IPI')):
                if (resultadoDET[item]['imposto']['IPI'].has_key('cEnq')): ipi_classe_enquadramentoImp = resultadoDET[item]['imposto']['IPI']['cEnq']
                else: ipi_classe_enquadramentoImp = None

                if (resultadoDET[item]['imposto']['IPI'].has_key('IPINT')): ipiVar = 'IPINT'
                elif (resultadoDET[item]['imposto']['IPI'].has_key('IPITrib')): ipiVar = 'IPITrib'

                if (resultadoDET[item]['imposto']['IPI'][ipiVar].has_key('CST')): ipi_cstImp = resultadoDET[item]['imposto']['IPI'][ipiVar]['CST']
                else: ipi_cstImp = None

                if (resultadoDET[item]['imposto']['IPI'][ipiVar].has_key('pIPI')): ipi_aliquotaImp = resultadoDET[item]['imposto']['IPI'][ipiVar]['pIPI']
                else: ipi_aliquotaImp = None
                
                if (resultadoDET[item]['imposto']['IPI'][ipiVar].has_key('vBC')): ipi_valor_base_calcImp = resultadoDET[item]['imposto']['IPI'][ipiVar]['vBC']
                else: ipi_valor_base_calcImp = None

                if (resultadoDET[item]['imposto']['IPI'][ipiVar].has_key('vIPI')): ipi_valorImp = resultadoDET[item]['imposto']['IPI'][ipiVar]['vIPI']
                else: ipi_valorImp = None
            else:
                ipi_classe_enquadramentoImp = None
                ipi_cstImp = None
                ipi_aliquotaImp = None
                ipi_valor_base_calcImp = None
                ipi_valorImp = None

            if (resultadoDET[item]['imposto'].has_key('PIS')):
                if (resultadoDET[item]['imposto']['PIS'][pisVar].has_key('CST')): pis_cstImp = resultadoDET[item]['imposto']['PIS'][pisVar]['CST']
                else: pis_cstImp = None

                if (resultadoDET[item]['imposto']['PIS'][pisVar].has_key('vBC')): pis_base_calcImp = resultadoDET[item]['imposto']['PIS'][pisVar]['vBC']
                else: pis_base_calcImp = None

                if (resultadoDET[item]['imposto']['PIS'][pisVar].has_key('pPIS')): pis_aliquotaImp = resultadoDET[item]['imposto']['PIS'][pisVar]['pPIS']
                else: pis_aliquotaImp = None

                if (resultadoDET[item]['imposto']['PIS'][pisVar].has_key('vPIS')): pis_valorImp = resultadoDET[item]['imposto']['PIS'][pisVar]['vPIS']
                else: pis_valorImp = None
            else:
                pis_cstImp = None
                pis_base_calcImp = None
                pis_aliquotaImp = None
                pis_valorImp = None

            if (resultadoDET[item]['imposto'].has_key('COFINS')):
                if (resultadoDET[item]['imposto']['COFINS'][cofinsVar].has_key('CST')): cofins_cstImp = resultadoDET[item]['imposto']['COFINS'][cofinsVar]['CST']
                else: cofins_cstImp = None

                if (resultadoDET[item]['imposto']['COFINS'][cofinsVar].has_key('vBC')): cofins_base_calcImp = resultadoDET[item]['imposto']['COFINS'][cofinsVar]['vBC']
                else: cofins_base_calcImp = None

                if (resultadoDET[item]['imposto']['COFINS'][cofinsVar].has_key('pCOFINS')): confins_aliquotaImp = resultadoDET[item]['imposto']['COFINS'][cofinsVar]['pCOFINS']
                else: confins_aliquotaImp = None

                if (resultadoDET[item]['imposto']['COFINS'][cofinsVar].has_key('vCOFINS')): cofins_valorImp = resultadoDET[item]['imposto']['COFINS'][cofinsVar]['vCOFINS']
                else: cofins_valorImp = None
            else:
                cofins_cstImp = None
                cofins_base_calcImp = None
                confins_aliquotaImp = None
                cofins_valorImp = None

            icms_st_bc_perc_reducaoImp = None 
            icms_st_perc_marg_valorImp = None
            icms_perc_reducao_base_calcImp = None

            pis_aliquota_percImp = None
            pis_qtd_vendidasImp = None
            pis_st_base_calcImp = None 
            pis_st_aliquota_percImp = None 
            pis_st_aliquotaImp = None 
            pis_st_qtd_vendidasImp = None 
            pis_st_valorImp = None
            
            cofins_aliquota_percImp = None
            cofins_qtd_vendidasImp = None 
            cofins_st_base_calcImp = None 
            cofins_st_aliquota_percImp = None 
            cofins_st_aliquotaImp = None 
            cofins_st_qtd_vendidasImp = None 
            cofins_st_valorImp = None 
            
            ipi_cod_enquadramentoImp = None 
            ipi_cnpj_produtorImp = None 
            ipi_cod_selo_controleImp = None 
            ipi_qtd_selo_controleImp = None 
            ipi_tipo_calcImp = None  
            ipi_qtd_total_unid_padraoImp = None 
            ipi_valor_unidImp = None 
            
            imp_import_base_calcImp = None 
            imp_import_depesas_aduaneirasImp = None 
            imp_import_IOFImp = None 
            imp_import_valorImp = None
            
            issqn_tributarioImp = None 
            issqn_valor_base_calcImp = None 
            issqn_aliquotaImp = None 
            issqn_list_servicosImp = None 
            issqn_ufImp = None 
            issqn_municipio_ocorrenciaImp = None 
            issqn_valor = None
                
            ##### Insert de Tipo de Produto #####

            verifTProd = i.execute("SELECT id FROM tipo_produto WHERE ncm='%s'" % (ncmTProd))

            if (verifTProd == 0):
                i.execute("INSERT INTO tipo_produto VALUES(NULL,'%s')" % (ncmTProd))
                idTProd = i.lastrowid
            else:
                listagem = i.fetchall()
                idTProd = long(listagem[0][0])

            ##### Insert de Produto #####

            verifProd = j.execute("SELECT id FROM produto WHERE cnpj='%s' AND cod_produto='%s'" % (cnpjEmit, cod_produtoProd))

            if (verifProd == 0):
                j.execute("INSERT INTO produto VALUES(NULL,%s,%s,%s,%s)" , (idTProd, cnpjEmit, produtoProd, cod_produtoProd))
                idProd = j.lastrowid
            else:
                listagem = j.fetchall()
                idProd = long(listagem[0][0])

            ##### Insert de Item NF #####

            k.execute("INSERT INTO item_nf VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (idNfe, idProd, quantidadeINF, unid_comercialINF, valorINF, cod_exp_tipiINF, cfopINF, outras_despesasINF, descontoINF, freteINF, seguroINF, indicador_comp_nfeINF, cod_ean_comercialINF, cod_ean_tributavelINF, unid_tributavelINF, quant_tributavelINF, valor_unitario_tribINF, valor_unitario_comINF, numero_pedidoINF, item_pedidoINF, valor_aprox_tributosINF, fciINF))
            idINF = k.lastrowid

            ##### Insert de Tipo de Imposto #####

            verifTImp = l.execute("SELECT id FROM tipo_imposto WHERE nome='%s'" % (nomeTImp))

            if (verifTImp ==0):
                l.execute("INSERT INTO tipo_imposto VALUES(NULL,%s)" , (nomeTImp))
                idTImp = l.lastrowid
            else:
                listagem = l.fetchall()
                idTImp = long(listagem[0][0])

            ##### Insert de Imposto #####

            m.execute("INSERT INTO imposto VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (idTImp, icms_cstImp, icms_origemImp, icms_alicota_aplic_calc_credImp, icms_valor_cred_aprovImp, icms_mod_det_base_calcImp, icms_perc_reducao_base_calcImp, icms_valor_base_calcImp, icms_aliquotaImp, icms_valorImp, icms_st_mod_BC_ICMS_STImp, icms_st_bc_perc_reducaoImp, icms_st_perc_marg_valorImp, icms_st_base_calcImp, icms_st_aliquotaImp, icms_st_valorImp, icms_st_base_calc_retido_anteriormenteImp, icms_st_valor_retido_anteriormenteImp, ipi_classe_enquadramentoImp, ipi_cod_enquadramentoImp, ipi_cnpj_produtorImp, ipi_cod_selo_controleImp, ipi_qtd_selo_controleImp, ipi_tipo_calcImp, ipi_valor_base_calcImp, ipi_aliquotaImp, ipi_qtd_total_unid_padraoImp, ipi_valor_unidImp, ipi_valorImp, ipi_cstImp, pis_cstImp, pis_base_calcImp, pis_aliquota_percImp, pis_aliquotaImp, pis_valorImp, pis_qtd_vendidasImp, cofins_cstImp, cofins_base_calcImp, cofins_aliquota_percImp, confins_aliquotaImp, cofins_valorImp, cofins_qtd_vendidasImp, pis_st_base_calcImp, pis_st_aliquota_percImp, pis_st_aliquotaImp, pis_st_qtd_vendidasImp, pis_st_valorImp, cofins_st_base_calcImp, cofins_st_aliquota_percImp, cofins_st_aliquotaImp, cofins_st_qtd_vendidasImp, cofins_st_valorImp, imp_import_base_calcImp, imp_import_depesas_aduaneirasImp, imp_import_IOFImp, imp_import_valorImp, issqn_tributarioImp, issqn_valor_base_calcImp, issqn_aliquotaImp, issqn_list_servicosImp, issqn_ufImp, issqn_municipio_ocorrenciaImp, issqn_valor))
            idImp = m.lastrowid

            ##### Insert de Imposto de Item NF #####

            verifImpNF = n.execute("SELECT id FROM imposto_item_nf WHERE idImposto='%d' AND idItem_nf='%d'" % (idImp, idINF))

            if (verifImpNF == 0):
                n.execute("INSERT INTO imposto_item_nf VALUES(NULL,%s,%s)" , (idImp, idINF))
                idImpNF = n.lastrowid
            else:
                listagem = n.fetchall()
                idImpNF = long(listagem[0][0])
                
    except MySQLdb.Error,err:
        con.rollback()
        
        c.close()
        d.close()
        e.close()
        f.close()
        g.close()
        h.close()
        i.close()
        j.close()
        k.close()
        l.close()
        m.close()
        n.close()
        
        con.close()

        sys.exit(2)
            
        
    ##### Fechar conexão #####

    con.commit()
    
    c.close()
    d.close()
    e.close()
    f.close()
    g.close()
    h.close()
    i.close()
    j.close()
    k.close()
    l.close()
    m.close()
    n.close()
    
    con.close()

i = 0
total = 0
endereco = './Notas/'
for empresa in os.listdir(endereco):
    if len(empresa)==14:
        for nota in os.listdir(endereco+"/"+empresa):
            if len(nota)==48:
                print nota
                i = i + 1
                doc = parse(endereco+"/"+empresa+"/"+nota)
                xml = doc.documentElement.getElementsByTagName("NFe")[0]
                xmlNota = xml.getElementsByTagName("infNFe")[0]
                inserirNota(xmlNota)
        #print "Empresa: ", empresa, " - Notas: ",i
        total = total + i
        i=0
print "\n Total: ", total
