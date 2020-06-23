
from ansible_collections.ibm.ibm_zos_core.plugins.module_utils.better_arg_parser import BetterArgParser # pylint: disable=import-error

# #Retrieves customer input and translates it and puts them into a dictionary to pass into the DatasetDefinition class
  #Used if the arguments the customer passes in differs from the arguments for DatasetDefinition. For example:
  #If the ansible module argument for block size is "blocksize", but DatasetDefinition takes in "block_size"
# def dataset_argument_generator(parsed_args):
#     kwargs = dict(dataset_name = parsed_args.get('name'),
#                      disposition = parsed_args.get('disposition'),
#                      type = parsed_args.get('type'),
#                      primary = parsed_args.get('primary'),
#                      primary_unit = parsed_args.get('primary_unit'),
#                      secondary = parsed_args.get('secondary'),
#                      secondary_unit = parsed_args.get('secondary_unit'),
#                      normal_disposition = parsed_args.get('normal_disposition'),
#                      conditional_disposition = parsed_args.get('conditional_disposition'),
#                      block_size = parsed_args.get('block_size'),
#                      record_format = parsed_args.get('record_format'),
#                      record_length = parsed_args.get('record_length'),
#                      storage_class = parsed_args.get('storage_class'),
#                      data_class = parsed_args.get('data_class'),
#                      management_class = parsed_args.get('management_class'),
#                      key_length = parsed_args.get('key_length'),
#                      key_offset = parsed_args.get('key_offset'),
#                      volumes = parsed_args.get('volumes'),
#                      dataset_key_label = parsed_args.get('dataset_key_label'),
#                      key_label1 = parsed_args.get('key_label1'),
#                      key_encoding1 = parsed_args.get('key_encoding1'),
#                      key_label2 = parsed_args.get('key_label2'),
#                      key_encoding2 = parsed_args.get('key_encoding2')
#                      )
#     return kwargs




def validate_input(module, result):
    try:
      module_defs = dict(
        irlm_enabled=dict(arg_type="bool", required=False),
        irlm_id=dict(arg_type="str", required=False),
        reslib=dict(arg_type="data_set", required=False),
        buffer_pool_param_dataset=dict(arg_type="data_set", required=False),
        primary_log_dataset=dict(arg_type="dict", options=dict(dataset_name=dict(arg_type="data_set", required=True),
                                                               dispositon=dict(arg_type="str", required=False, choices=['EXCL','OLD','SHR','NEW']),
                                                               primary=dict(arg_type="int", required=False),
                                                               primary_unit=dict(arg_type="str", required=False, choices=['K', 'KB', 'M', 'MB', 'G', 'GB', 'C', 'CYL', 'T', 'TRK']),
                                                               secondary=dict(arg_type="int", required=False),
                                                               secondary_unit=dict(arg_type="str", required=False, choices=['K', 'KB', 'M', 'MB', 'G', 'GB', 'C', 'CYL', 'T', 'TRK']),
                                                               normal_disposition=dict(arg_type="str", required=False, choices=['KEEP', 'DELETE', 'CATLG', 'UNCATLG']),
                                                               conditional_disposition=dict(arg_type="str", required=False, choices=['KEEP', 'DELETE', 'CATLG', 'UNCATLG']),
                                                               record_format=dict(arg_type="str", required=False, choices=['FB', 'VB', 'FBA', 'VBA', 'U']),
                                                               record_length=dict(arg_type="int", required=False),
                                                               block_size=dict(arg_type="int", required=False)
                                                              ),
                                       required=False),
        secondary_log_dataset=dict(arg_type="dict", options=dict(dataset_name=dict(arg_type="data_set", required=True),
                                                                 dispositon=dict(arg_type="str", required=False, choices=['EXCL','OLD','SHR','NEW']),
                                                                 primary=dict(arg_type="int", required=False),
                                                                 primary_unit=dict(arg_type="str", required=False, choices=['K', 'KB', 'M', 'MB', 'G', 'GB', 'C', 'CYL', 'T', 'TRK']),
                                                                 secondary=dict(arg_type="int", required=False),
                                                                 secondary_unit=dict(arg_type="str", required=False, choices=['K', 'KB', 'M', 'MB', 'G', 'GB', 'C', 'CYL', 'T', 'TRK']),
                                                                 normal_disposition=dict(arg_type="str", required=False, choices=['KEEP', 'DELETE', 'CATLG', 'UNCATLG']),
                                                                 conditional_disposition=dict(arg_type="str", required=False, choices=['KEEP', 'DELETE', 'CATLG', 'UNCATLG']),
                                                                 record_format=dict(arg_type="str", required=False, choices=['FB', 'VB', 'FBA', 'VBA', 'U']),
                                                                 record_length=dict(arg_type="int", required=False),
                                                                 block_size=dict(arg_type="int", required=False)
                                                                ), 
                                        required=False),
        psb_lib=dict(arg_type="data_set", required = False),
        dbd_lib=dict(arg_type="data_set", required = False),
        check_timestamp=dict(arg_type="bool", required=False),
        acb_lib=dict(arg_type="list", elements="data_set", required=True),
        bootstrap_dataset=dict(arg_type="data_set", required = False),
        directory_datasets=dict(arg_type="list", elements="data_set", required=False),
        temp_acb_dataset=dict(arg_type="data_set", required = False),
        directory_staging_dataset=dict(arg_type="data_set", required = False),
        proclib=dict(arg_type="data_set", required = False),
        steplib=dict(arg_type="data_set", required = False),
        sysabend=dict(arg_type="data_set", required = False),
        sysprint=dict(arg_type="data_set", required=False),
        control_statements=dict(arg_type="dict", options=dict(duplist=dict(arg_type="bool", required=False),
                                                              errormax=dict(arg_type="int", required=False),
                                                              resource_chkp_freq=dict(arg_type="int", required=False),
                                                              segment_chkp_freq=dict(arg_type="int", required=False),
                                                              isrtlist=dict(arg_type="bool", required=False),
                                                              managed_acbs=dict(arg_type="dict", 
                                                                required=False, 
                                                                options=dict(setup=dict(arg_type="bool", required=False),
                                                                             stage=dict(arg_type=dict, required=False, 
                                                                               options=dict(latest=dict(arg_type="bool", required=False),
                                                                                       uncond=dict(arg_type="bool", required=False),
                                                                                       delete=dict(arg_type="bool", required=False),
                                                                                       gsampcb=dict(arg_type="bool", required=False),
                                                                                       gsamdbd=dict(arg_type="str", required=False)
                                                                                    )
                                                                                ),
                                                                              update=dict(arg_type=dict, required=False, 
                                                                                options=dict(latest=dict(arg_type="bool", required=False),
                                                                                       uncond=dict(arg_type="bool", required=False),
                                                                                       share=dict(arg_type="bool", required=False),
                                                                                       gsampcb=dict(arg_type="bool", required=False),
                                                                                       gsamdbd=dict(arg_type="str", required=False)
                                                                                    )
                                                                              )
                                                                      )
                                                                  ),
                                                              no_isrtlist=dict(arg_type="bool", required=False)),
                                        required=False)
      )

      parser = BetterArgParser(module_defs)
      parsed_args = parser.parse_args(module.params)

      if parsed_args['directory_staging_dataset'] is not None:
        validate_directory_staging_dataset(parsed_args['directory_datasets'], result, module)


      return parsed_args
    except ValueError as error:
      result['msg'] = error.args
      result['rc']=1
      module.fail_json(**result)

def validate_directory_staging_dataset(dset, result, module):
    if len(dset) > 20:
      result['msg'] = "You cannot specify more than 20 IMS directory datasets"
      module.fail_json(**result)


def parse_control_statements(controlStatements):
    controlStr=[]
    if controlStatements['duplist']:
        controlStr.append("DUPLIST")
    if controlStatements['errormax']:
        controlStr.append("ERRORMAX="+ str(controlStatements['errormax']))
    if controlStatements['resource_chkp_freq']:
        controlStr.append("RESOURCE_CHKP_FREQ="+str(controlStatements['resource_chkp_freq']))
    if controlStatements['segment_chkp_freq']:
        controlStr.append("SEGMENT_CHKP_FREQ="+str(controlStatements['resource_chkp_freq']))
    if controlStatements['isrtlist']:
        controlStr.append("ISRTLIST")
    if controlStatements['no_isrtlist']:
        controlStr.append("NOISRTLIST")

    managed_acbs_string=[]
    managed_acbs=controlStatements['managed_acbs']
    if managed_acbs:
      managed_acbs_string.append("MANAGEDACBS=")
      if managed_acbs['setup']:
        managed_acbs_string.append("SETUP")
        controlStr.append("".join(managed_acbs_string))
        print("util printing control string: " + " ".join(controlStr))
        return controlStr
      if managed_acbs['stage']:
        managed_acbs_string.append("STAGE")
        if managed_acbs['stage']['gsamdbd']:
          managed_acbs_string.append(",GSAM=" + managed_acbs['stage']['gsamdbd'])
        if managed_acbs['stage']['latest']:
          managed_acbs_string.append(",LATEST")
        elif managed_acbs['stage']["uncond"]:
          managed_acbs_string.append(",UNCOND")
        if managed_acbs['stage']["delete"]:
          managed_acbs_string.append(",DELETE")
        if managed_acbs['stage']['GSAMPCB']:
          managed_acbs_string.append(",GSAMPCB")
        controlStr.append("".join(managed_acbs_string))
        print("util printing control string: " + " ".join(controlStr))
        return controlStr
      if managed_acbs['update']:
        managed_acbs_string.append("UPDATE")
        if managed_acbs['update']['gsamdbd']:
          managed_acbs_string.append(",GSAM=" + managed_acbs['stage']['gsamdbd'])
        if managed_acbs['update']['latest']:
          managed_acbs_string.append(",LATEST")
        elif managed_acbs['update']["uncond"]:
          managed_acbs_string.append(",UNCOND")
        if managed_acbs['update']["share"]:
          managed_acbs_string.append(",SHARE")
        if managed_acbs['update']['GSAMPCB']:
          managed_acbs_string.append(",GSAMPCB")
        controlStr.append("".join(managed_acbs_string))
        print("util printing control string: " + controlStr)
        return controlStr
    
    controlStr.append("".join(managed_acbs_string))
    print("util printing control string: " + " ".join(controlStr))
    return controlStr