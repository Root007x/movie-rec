mkdir -p ~/.streamlit/

echo "\
[server]\n\
prot = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml