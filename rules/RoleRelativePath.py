from ansiblelint import AnsibleLintRule


format = "{}"

class RoleRelativePath(AnsibleLintRule):
    id = 'E201'
    shortdesc = "Doesn't need a relative path in role"
    description = ''
    tags = ['role']

    def matchplay(self, file, play):
        # assume if 'roles' in path, inside a role.
        if 'roles' not in file['path']:
            return []
        if 'template' in play:
            if not isinstance(play['template'], dict):
                return False
            if "../templates" in play['template']['src']:
                return [({'': play['template']},
                                self.shortdesc)]
        if 'win_template' in play:
            if not isinstance(play['win_template'], dict):
                return False
            if "../win_templates" in play['win_template']['src']:
                return ({'win_template': play['win_template']},
                                self.shortdesc)
        if 'copy' in play:
            if not isinstance(play['copy'], dict):
                return False
            if 'src' in play['copy']:
                if "../files" in play['copy']['src']:
                    return ({'sudo': play['copy']},
                                self.shortdesc)
        if 'win_copy' in play:
            if not isinstance(play['win_copy'], dict):
                return False
            if "../files" in play['win_copy']['src']:
                return ({'sudo': play['win_copy']},
                                self.shortdesc)
        return []
