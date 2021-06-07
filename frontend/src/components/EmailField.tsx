import React from 'react'
import { fade } from '@material-ui/core/styles'

import { InputBase } from '@material-ui/core'

import theme from '../../styles/theme'

import { AUTHOR_NAME_LOCAL_STORAGE_KEY } from '../constants'
import useLocalStorage from '../hooks/useLocalStorage'

const EmailField = () => {
  const [authorName, setAuthorName] = useLocalStorage<string>(
    AUTHOR_NAME_LOCAL_STORAGE_KEY
  )

  return (
    <div
      style={{
        backgroundColor: fade(theme.palette.common.white, 0.15),
        color: theme.palette.common.white,
        borderRadius: 4,
        padding: theme.spacing(0.25, 2),
      }}
    >
      <InputBase
        placeholder="Your name..."
        style={{ color: 'inherit' }}
        value={authorName}
        onChange={(e) => setAuthorName(e.target.value)}
      />
    </div>
  )
}

export default EmailField
