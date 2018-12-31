import os

# extract path to the config file
pwd_config_file = os.path.realpath(__file__)
config_file_path = '/'.join(pwd_config_file.split('/')[:-1])

# specify full path to corresponding executables at the right side of colon
config_dict = {'prodigal'     :  'prodigal',
               'hmmsearch'    :  'hmmsearch',
               'hmmfetch'     :  'hmmfetch',
               'hmmalign'     :  'hmmalign',
               'hmmstat'      :  'hmmstat',
               'mafft'        :  'mafft',
               'fasttree'     :  'FastTree',
               'blastp'       :  'blastp',
               'blastn'       :  'blastn',
               'makeblastdb'  :  'makeblastdb',
               'ranger_mac'   :  'Ranger-DTL-Dated.mac',
               'ranger_linux' :  'Ranger-DTL-Dated.linux',
               'path_to_hmm'  :  '%s/MetaCHIP_phylo.hmm'    % config_file_path,  # do not edit this line
               'circos_HGT_R' :  '%s/MetaCHIP_circos_HGT.R' % config_file_path   # do not edit this line
               }
