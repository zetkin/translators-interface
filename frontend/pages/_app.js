import React from 'react'
import Head from 'next/head'

import { ThemeProvider, fade } from '@material-ui/core/styles'
import CssBaseline from '@material-ui/core/CssBaseline'
import { AppBar, Toolbar, Typography, InputBase } from '@material-ui/core'

import theme from '../styles/theme'
import { AUTHOR_NAME_LOCAL_STORAGE_KEY } from '../src/constants'
import useLocalStorage from '../src/hooks/useLocalStorage'

export default function MyApp(props) {
  const { Component, pageProps } = props
  const [authorName, setAuthorName] = useLocalStorage(
    AUTHOR_NAME_LOCAL_STORAGE_KEY
  )

  React.useEffect(() => {
    // Remove the server-side injected CSS.
    const jssStyles = document.querySelector('#jss-server-side')
    if (jssStyles) {
      jssStyles.parentElement.removeChild(jssStyles)
    }
  }, [])

  return (
    <React.Fragment>
      <Head>
        <title>My page</title>
        <meta
          name="viewport"
          content="minimum-scale=1, initial-scale=1, width=device-width"
        />
      </Head>
      <ThemeProvider theme={theme}>
        <CssBaseline />

        <AppBar position="static">
          <Toolbar variant="dense" style={{ justifyContent: 'space-between' }}>
            <Typography variant="h6">Zetkin Translators Interface</Typography>
            {/* Username Field */}
            <div
              style={{
                backgroundColor: fade(theme.palette.common.white, 0.15),
                color: theme.palette.common.white,
                borderRadius: 4,
                padding: theme.spacing(0.25, 2),
              }}
            >
              <InputBase
                variant="outlined"
                placeholder="Your name..."
                style={{ color: 'inherit' }}
                value={authorName}
                onChange={(e) => setAuthorName(e.target.value)}
              />
            </div>
          </Toolbar>
        </AppBar>

        <Component {...pageProps} />
      </ThemeProvider>
    </React.Fragment>
  )
}
