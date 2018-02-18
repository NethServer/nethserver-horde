<?php
$conf['user']['allow_view_source'] = true;
$conf['server']['server_list'] = 'none';
$conf['compose']['use_vfs'] = false;
$conf['compose']['link_attachments'] = false;
$conf['compose']['attach_size_limit'] = 0;
$conf['compose']['attach_count_limit'] = 0;
$conf['compose']['reply_limit'] = 200000;
$conf['compose']['ac_threshold'] = 3;
$conf['compose']['htmlsig_img_size'] = 30000;
$conf['pgp']['keylength'] = 0;
$conf['maillog']['driver'] = 'history';
$conf['sentmail']['driver'] = 'Null';
$conf['contactsimage']['backends'] = array('IMP_Contacts_Avatar_Addressbook', 'IMP_Contacts_Avatar_Gravatar');
$conf['tasklist']['use_tasklist'] = true;
$conf['notepad']['use_notepad'] = true;
