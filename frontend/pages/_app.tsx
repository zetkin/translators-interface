import React from 'react'
import Head from 'next/head'

import type { AppProps } from 'next/app'

import { ThemeProvider } from '@material-ui/core/styles'
import CssBaseline from '@material-ui/core/CssBaseline'
import { AppBar, Toolbar, Typography, Link } from '@material-ui/core'

import theme from '../styles/theme'
import EmailField from '../src/components/EmailField'
import { UserEmailProvider } from '../src/contexts/userEmailContext'

export default function MyApp({ Component, pageProps }: AppProps) {
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
      <UserEmailProvider>
        <ThemeProvider theme={theme}>
          <CssBaseline />

          <AppBar position="static">
            <Toolbar
              variant="dense"
              style={{ justifyContent: 'space-between' }}
            >
              <Link href="/" color="inherit" underline="none">
                <Typography variant="h6">
                  Zetkin Translators Interface
                </Typography>
              </Link>
              <EmailField />
            </Toolbar>
          </AppBar>

          <Component {...pageProps} />
        </ThemeProvider>
      </UserEmailProvider>
    </React.Fragment>
  )
}
