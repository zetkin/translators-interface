import React, { useState } from 'react'
import { Button, TextField } from '@material-ui/core'

import { Translation, TranslationPostBody } from '../global.types'
import { postTranslation } from '../api/translations'

interface Props {
  base: Translation
  selected: Translation
}

const TranslationField = ({base, selected}: Props) => {
  const [error, setError] = useState<string>()
  const [savedValue, setSavedValue] = useState<string>(selected?.text)
  const [value, setValue] = useState<string>(selected?.text)

  const handleSave = async () => {
    setError(null)
    // Build request body
    const body: TranslationPostBody = {
      ...base,
      author: 'river',
      from_repository: false,
      language: selected.language.id,
      file_path: selected.file_path,
      text: value,
    }

    // Make request
    try {
      const req = await postTranslation(body)
      setSavedValue(value)
    } catch (e) {
      setError('Could not save')
      console.error('Error posting!')
    }
  }
  
  return (
    <div style={{display: 'flex'}}>
      <TextField 
        error={error != null}
        label={error || null}
        style={{width: '100%'}} 
        variant="outlined" 
        defaultValue={savedValue} 
        onInput={(e) => {
          e.preventDefault()
          setError(null)
          // @ts-ignore
          setValue(e.target.value)
        }}
      />
      {value != savedValue && (
        <Button variant="contained" color="secondary" disableElevation onClick={handleSave}>Save</Button>
      )}
      </div>
  )
}

export default TranslationField