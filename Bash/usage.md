1. Download file:
  * From remote server: Rsync
  * From remote server: Scp
  * From hosted file URL: Curl
    * curl -O file_url
 
2. Define execuable function:
  * in ~/bash_profile (MacOS), e.g. 
  ```
    function get_sts_token
    {
            some_function_to_get_sts_token()
  	  aws configure set aws_access_key_id "$(aws configure get aws_access_key_id --profile <profile_name>)" --profile default
  	  aws configure set aws_secret_access_key "$(aws configure get aws_secret_access_key --profile <profile_name>)" --profile default
  	  aws configure set aws_session_token "$(aws configure get aws_session_token --profile <profile_name>)" --profile default
    	  aws configure set aws_security_token "$(aws configure get aws_security_token --profile <profile_name>)" --profile default
    }
  ```
  
3. Define and use variable
   * define: export some_variable = some_value
   * use: $some_variable
  
4. Debug a bash script
   * $bash -x <script_name>

5. Insert or replace text
   * Insert text after reg match `sed -i /<match_text>/a<insert_text> file.txt`
   * Replace text after reg match `sed -i /<match_text>/c<replace_text> file.txt` 

6. Save command result to a variable
   * some_var=$(some_command)
