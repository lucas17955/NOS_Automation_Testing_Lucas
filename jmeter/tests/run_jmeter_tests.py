import os
import subprocess
from datetime import datetime
import sys

# Ensure the current working directory is in the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_dir)

import utils.config as config

def replace_auth_token_in_jmx(jmx_path, token):
    # Read the JMX file
    with open(jmx_path, 'r', encoding='utf-8') as file:
        jmx_content = file.read()
    
    # Replace the AUTH_TOKEN placeholder
    jmx_content = jmx_content.replace('AUTH_TOKEN', token)
    
    # Write the modified content to a new file
    modified_jmx_path = jmx_path.replace('.jmx', '_modified.jmx')
    with open(modified_jmx_path, 'w', encoding='utf-8') as file:
        file.write(jmx_content)
    
    return modified_jmx_path

def run_jmeter_test():
    # Define the paths
    project_dir = os.path.dirname(os.path.dirname(__file__))
    jmeter_home = os.path.join(project_dir, 'apache-jmeter-5.6.3')
    jmeter_bin = os.path.join(jmeter_home, 'bin', 'jmeter.bat') #.bat for using windows
    test_plan = os.path.join(project_dir, 'projects', 'get_user_stress_test.jmx')
    log_file = os.path.join(project_dir, 'results', 'jmeter.log')
    properties_file = os.path.join(project_dir, 'configs', 'jmeter.properties')
    
    # Create the results directory if it doesn't exist
    results_dir = os.path.join(project_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)
    
    # Generate a timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Define the output JTL file path with timestamp
    output_jtl = f'results_{timestamp}.jtl'
    output_jtl_path = os.path.join(results_dir, output_jtl)

    # Define the HTML report output directory
    html_report_dir = os.path.join(results_dir, f'html_report_{timestamp}')
    os.makedirs(html_report_dir, exist_ok=True)

    # Check if JMeter home is set correctly
    if not os.path.exists(jmeter_bin):
        raise FileNotFoundError(f'JMeter binary not found at {jmeter_bin}')
    
    # Check if the test plan exists
    if not os.path.exists(test_plan):
        raise FileNotFoundError(f'Test plan not found at {test_plan}')
    
    # Check if the properties file exists
    if not os.path.exists(properties_file):
        raise FileNotFoundError(f'Properties file not found at {properties_file}')
    
    # Replace the AUTH_TOKEN placeholder in the JMX file
    modified_test_plan = replace_auth_token_in_jmx(test_plan, config.AUTH_TOKEN)
    
    # Build the JMeter command
    cmd = [
        jmeter_bin,
        '-n',  # Non-GUI mode
        '-t', modified_test_plan,  # Test plan
        '-l', output_jtl_path,  # JTL output file
        '-j', log_file,  # Log file
        '-p', properties_file,  # JMeter properties
        '-e',  # Generate HTML report
        '-o', html_report_dir  # Output directory for HTML report
    ]
    
    # Run the JMeter command
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Print the output
    print("JMeter STDOUT:", result.stdout)
    print("JMeter STDERR:", result.stderr)

    # Check for errors
    if result.returncode != 0:
        raise Exception(f'JMeter test failed with return code {result.returncode}')

if __name__ == "__main__":
    run_jmeter_test()