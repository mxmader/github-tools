# Get all repos by organization name

Useful reference code for cloning all repos of an organization.

Example 1:

```console
[joe@localhost github-tools]$ ./get_repo_list_by_org.py openshift
Found: rhc - clone URL: git@github.com:openshift/rhc.git
Found: django-example - clone URL: git@github.com:openshift/django-example.git
Found: rails-example - clone URL: git@github.com:openshift/rails-example.git
Found: cakephp-example - clone URL: git@github.com:openshift/cakephp-example.git
Found: wordpress-example - clone URL: git@github.com:openshift/wordpress-example.git
Found: sinatra-example - clone URL: git@github.com:openshift/sinatra-example.git
Found: piwik-openshift-quickstart - clone URL: git@github.com:openshift/piwik-openshift-quickstart.git
Found: flask-example - clone URL: git@github.com:openshift/flask-example.git
Found: joomla-example - clone URL: git@github.com:openshift/joomla-example.git
Found: openshift-java-client - clone URL: git@github.com:openshift/openshift-java-client.git
Found: jboss-as7-modules - clone URL: git@github.com:openshift/jboss-as7-modules.git
Found: CodeIgniterQuickStart - clone URL: git@github.com:openshift/CodeIgniterQuickStart.git
Found: openshift.github.com - clone URL: git@github.com:openshift/openshift.github.com.git
Found: magento-example - clone URL: git@github.com:openshift/magento-example.git
Found: openshift-diy-binhello-demo - clone URL: git@github.com:openshift/openshift-diy-binhello-demo.git
Found: kitchensink-example - clone URL: git@github.com:openshift/kitchensink-example.git
Found: python-interface - clone URL: git@github.com:openshift/python-interface.git
Found: etherpad-example - clone URL: git@github.com:openshift/etherpad-example.git
Found: dokuwiki-quickstart - clone URL: git@github.com:openshift/dokuwiki-quickstart.git
Found: origin-server - clone URL: git@github.com:openshift/origin-server.git
Found: jenkins-cloud-plugin - clone URL: git@github.com:openshift/jenkins-cloud-plugin.git
Found: spring-eap6-quickstart - clone URL: git@github.com:openshift/spring-eap6-quickstart.git
Found: test-pull-requests - clone URL: git@github.com:openshift/test-pull-requests.git
Found: capedwarf-example - clone URL: git@github.com:openshift/capedwarf-example.git
Found: capedwarf-example-modules - clone URL: git@github.com:openshift/capedwarf-example-modules.git
Found: mod_vhost_choke - clone URL: git@github.com:openshift/mod_vhost_choke.git
Found: jboss-eap6-modules - clone URL: git@github.com:openshift/jboss-eap6-modules.git
Found: origin-dev-tools - clone URL: git@github.com:openshift/origin-dev-tools.git
Found: owncloud-openshift-quickstart - clone URL: git@github.com:openshift/owncloud-openshift-quickstart.git
Found: origin-community-cartridges - clone URL: git@github.com:openshift/origin-community-cartridges.git
```

Example 2:

```console
[joe@localhost github-tools]$ ./get_repo_list_by_org.py masterpeace
Found: foobar - clone URL: git@github.com:MasterPeace/foobar.git
```
