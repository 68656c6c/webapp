import os
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    vmn = request.form['vmname']
    osv = request.form['operation-system']
    vcpus = request.form['vmcpus']
    vmem = request.form['vmmemory']
    vdisksize = request.form['vmdisksize']
    creation = "ansible-playbook /etc/playbooks/vsphere-creation.yml -e vmtemplate={0} -e vmname={1} -e vm_cpus={2} -e vm_memory={3} -e disk_size={4} > /dev/null &".format(osv,vmn,vcpus,vmem,vdisksize)
    os.system(creation)
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
