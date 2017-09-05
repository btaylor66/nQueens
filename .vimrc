""""""""""""""""""""""
"     defaults       "
""""""""""""""""""""""

" easier paste mode
set pastetoggle=<F3>

" mouse and backspace
"set mouse=a  " on OSX press ALT and click

" mouse stuff for tmux
set ttymouse=xterm2

" make backspace behave like normal again
set bs=2

" .swp files, .swp files everywhere
set noswapfile
set nobackup
set nowritebackup

" tabs are spaces, ya dummy
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab
set smarttab

" can i still undo?
set undofile
set undodir=$HOME/.undo
set history=700
set undolevels=700

" searching
set incsearch " incremental search
set hlsearch " highlight search results
set ignorecase
set smartcase

" other set defaults
set encoding=utf-8
set hidden " hide buffers instead of closing them
set autoread " read outside file changes into buffer
set showmatch
set scrolloff=2 " scroll buffer
set splitbelow
set splitright



""""""""""""""""""""""
"   color & syntax   "
""""""""""""""""""""""


" line numbers and length
set number  " show line numbers
set tw=99   " width of document (used by gd)
set nowrap  " don't automatically wrap on load
set fo-=t   " don't automatically wrap text when typing
set colorcolumn=100

" automatically close autocompletion window
"autocmd CursorMovedI * if pumvisible() == 0|pclose|endif
"autocmd InsertLeave * if pumvisible() == 0|pclose|endif
"let g:AutoClosePumvisible = {"ENTER": "\<C-Y>", "ESC": "\<ESC>"}
