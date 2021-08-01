set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)

" ...

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" default space/tab stuff
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4

set splitbelow
set splitright

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Enable folding
set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za

" Code folding
Plugin 'tmhedberg/SimpylFold'
let g:SimpylFold_docstring_preview=1

" PEP 8 indentation
set colorcolumn=80
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=79 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

au BufNewFile,BufRead *.js, *.html, *.css
    \ set tabstop=2 |
    \ set softtabstop=2 |
    \ set shiftwidth=2

" Auto indentation
Plugin 'vim-scripts/indentpython.vim'

" Flag unnecessary whitespace
" au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

" UTF-8 support
set encoding=utf-8
set fileencoding=utf-8

" Autocomplete
"Bundle 'Valloric/YouCompleteMe'

"let g:ycm_autoclose_preview_window_after_completion=1
"map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" auto remove whitespace at end of lines when saving python file
if &ft == "python"
    autocmd VimEnter :20 sp fn
endif

" Python venv support
"py3 << EOF
"import os
"import sys
"if 'VIRTUAL_ENV' in os.environ:
"  project_base_dir = os.environ['VIRTUAL_ENV']
"  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
"  execfile(activate_this, dict(__file__=activate_this))
"EOF

" TODO: conda support

" Syntax checking and highlighting
Plugin 'vim-syntastic/syntastic'
Plugin 'nvie/vim-flake8'
let python_highlight_all=1
syntax on

" Color scheme
Plugin 'arcticicestudio/nord-vim'
colorscheme nord

" File browsing
Plugin 'scrooloose/nerdtree'

" hide .pyc from nerdtree
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree

" kitty terminal fix
if has('gui_running') || has('nvim')
    hi Normal 		guifg=#f6f3e8 guibg=#242424
else
    " Set the terminal default background and foreground colors, thereby
    " improving performance by not needing to set these colors on empty cells.
    hi Normal guifg=NONE guibg=NONE ctermfg=NONE ctermbg=NONE
    let &t_ti = &t_ti . "\033]10;#f6f3e8\007\033]11;#242424\007"
    let &t_te = &t_te . "\033]110\007\033]111\007"
endif

" Turn on line numbers
set nu

" Pretty status bar
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

" conda witin vim
Plugin 'cjrh/vim-conda'
