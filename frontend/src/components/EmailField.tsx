import React, { useState } from 'react'
import { fade } from '@material-ui/core/styles'

import { InputBase, Button, Tooltip } from '@material-ui/core'

import theme from '../../styles/theme'
import useLocalStorage from '../hooks/useLocalStorage'
import { AUTHOR_NAME_LOCAL_STORAGE_KEY } from '../constants'

import RegisterDialog from './RegisterDialog'

const EmailField = () => {
  const [authorEmail] = useLocalStorage<string>(AUTHOR_NAME_LOCAL_STORAGE_KEY)
  const [registerDialogOpen, setRegisterDialogOpen] = useState(false)

  return (
    <>
      <button
        style={{
          cursor: 'pointer',
          backgroundColor: fade(theme.palette.common.white, 0.15),
          color: theme.palette.common.white,
          borderRadius: 4,
          padding: theme.spacing(1, 2),
          border: 'none',
        }}
        onClick={(e) => {
          setRegisterDialogOpen(true)
        }}
      >
        <span style={{ color: 'inherit', fontSize: '1.1em' }}>
          {authorEmail || 'Your email...'}
        </span>
      </button>
      <RegisterDialog
        open={registerDialogOpen}
        onClose={() => {
          setRegisterDialogOpen(false)
        }}
      />
    </>
  )
}

export default EmailField
