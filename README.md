============
Nosecomplete
============

Nosecomplete is a nose plugin for completing test modules/classes/methods/functions from the command line.

Nosecomplete is composed of two pieces: a script called 'nosecomplete' and a shell completion function that calls the script.

An example using tab completion:

    % nosetests utils/test_decorators.py:Test<TAB>
    utils/test_decorators.py:TestCache
	utils/test_decorators.py:TestRetry

    % nosetests utils/test_decorators.py:TestRetry.<TAB>
    utils/test_decorators.py:TestRetry.test_eventual_success
	utils/test_decorators.py:TestRetry.test_expires_raises

An example calling nosecomplete directly:

	% nosecomplete utils/test_decorators.py:Test<ENTER>
    utils/test_decorators.py:TestCache
	utils/test_decorators.py:TestRetry

Installation
============

Install nosecomplete from pypi:

	pip install nosecomplete
	
Follow @alonhorev on twitter for updates.

bash
----

Add the following snippet to your .bashrc:

    # copied from newer versions of bash
    __ltrim_colon_completions() {
        # If word-to-complete contains a colon,
        # and bash-version < 4,
        # or bash-version >= 4 and COMP_WORDBREAKS contains a colon
        if [[
            "$1" == *:* && (
                ${BASH_VERSINFO[0]} -lt 4 || 
                (${BASH_VERSINFO[0]} -ge 4 && "$COMP_WORDBREAKS" == *:*) 
            )
        ]]; then
            # Remove colon-word prefix from COMPREPLY items
            local colon_word=${1%${1##*:}}
            local i=${#COMPREPLY[*]}
            while [ $((--i)) -ge 0 ]; do
                COMPREPLY[$i]=${COMPREPLY[$i]#"$colon_word"}
            done
        fi
    } # __ltrim_colon_completions()
    
    _nosetests() 
    {
        cur="${COMP_WORDS[COMP_CWORD]}"
        COMPREPLY=(`nosecomplete ${cur} 2>/dev/null`)
        __ltrim_colon_completions "$cur"
    }
    complete -o nospace -F _nosetests nosetests

zsh
---

Add the following snippet to your .zshrc:

    autoload -U compinit
    compinit
    
    autoload -U bashcompinit
    bashcompinit
    
    _nosetests() 
    {
        cur="${COMP_WORDS[COMP_CWORD]}"
        COMPREPLY=(`nosecomplete ${cur} 2>/dev/null`)
    }
    complete -o nospace -F _nosetests nosetests
