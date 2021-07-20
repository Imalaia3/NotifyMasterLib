import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom


class NotifyMasterLib():
  #Hi And Thanks For Using My Code Base! My Name Is Imalaia3! For Help Look Out For The D: In Comments!





  #D: simple_send() function. Sends a very simple message through PowerShell  It Has Some Args: simple_send(string title, string innertext)1
  def simple_send(toast_title, innertext):
    


    #D: Shameless plug here. You Have The Right To Remove This Line. But If You Want To Help Me Keep It In :)
    print("USING: IMALAIA3 CODEBASE: NOTIFYMASTER! github.com/imalaia3 imalaia3 on yt")


    #D: :rolf:
    app = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\WindowsPowerShell\\v1.0\\powershell.exe'



    #D: My Goal Is To Make This To A Standalone App With args and no powershell :/
    nManager = notifications.ToastNotificationManager
    notifier = nManager.create_toast_notifier(app)



    #D: <actions> = buttons n stuff. Simple Send Has Only 2: Delete And Dismiss
    tString = """
  <toast>
    <visual>
      <binding template='ToastGeneric'>
        <text>"""+toast_title+"""</text>
        <text>"""+innertext+"""</text>
      </binding>
    </visual>
    <actions>
      <action
        content="Delete"
        arguments="action=delete"/>
      <action
        content="Dismiss"
        arguments="action=dismiss"/>
    </actions>        
  </toast>
"""
    xDoc = dom.XmlDocument()
    xDoc.load_xml(tString)

    notifier.show(notifications.ToastNotification(xDoc))  
