* Global variable:
  * Terraform automatically loads all *.tf files in current directory but cannot refer to any variables outside of current directory. 
  * A work-around is to define a terraform.tfvars file storing all global variable, and create symlink to it in each directory, e.g. `current_dir$ ln -s ../global/terraform.tfvars .` __Note:__ terraform.tfvars only stores value of variable, variable itself still needs to be declared in either main.tf or variables.tf.
    * e.g. in terraforms.tfvars
       ``` ami = ami-1234567 ```
       in variables.tf
       ``` variable "ami" {description = "blahblahblah" type="string"} ```
 
 * Input Variable:
   * No matter what type of input variable is, variable needs to be declared in variables.tf(i.e. no value assignment just declaration)
   * For non-string variable declaration, 'type' needs to be specified.
 
 * Map of map:
   * map of map is not supported directly but can be split into two maps
   * e.g. 
     ``` 
     amis = {
        dev = {
          us-west-2 = "ami-abc123"
        }
        prod = {
          us-west-2 = "ami-cba321"
        }
      }
     }
     
     can be translate into this:
     
     amis = {
        dev = "amis_dev_map"
        prod = "amis_prod_map"
     }
     amis_dev_map = {
        us_west_2 = "ami-abc123"
      }
     }
     amis_prod_map = {
        us_west_2 = "ami-cba321"
     }
     ```
   
   * Map lookup:
     * `${lookup(var.map, var.index)}`
     or,
     * `${var.map[var.index]}`

* [Reference(Offcial)](https://terraformbook.com/TheTerraformBook_sample.pdf)
    
