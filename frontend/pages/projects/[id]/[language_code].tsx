import { GetStaticProps, GetStaticPaths, NextPage } from 'next'
import Head from 'next/head'
import Link from 'next/link'

import { Container, Typography, TextField, Card, CardContent, Table, TableHead, TableRow, TableCell, TableBody } from '@material-ui/core'

import { Translation, Project, Language } from '../../../src/global.types'
import { getProject, getProjects } from '../../../src/api/projects'
import TranslationField from '../../../src/components/TranslationField'
import { getTranslations } from '../../../src/api/translations'
import joinTranslations, { JoinedTranslation } from '../../../src/utils/joinTranslations'

/**
 * Translations Page - Page for viewing and editing translations
 */

interface StaticProps {
  project: Project,
  translations: Translation[],
  englishTranslations: Translation[],
  joinedTranslations: JoinedTranslation[]
  selectedLanguage: Language
}

export const getStaticPaths: GetStaticPaths = async () => {
  const projects = await getProjects()

  const paths = projects.reduce((acc, project) => {
    return [...acc, ...project.languages.map(language => `/projects/${project.id}/${language.language_code}`)]
  }, [])

  return {
    paths,
    fallback: true,
  }
}

export const getStaticProps: GetStaticProps<StaticProps, {id: string, language_code: string}> = async ({
  params,
}) => {
  const project = await getProject(params.id)

  const selectedLanguage = project.languages.find(language => language.language_code === params.language_code)
  const english = project.languages.find(language => language.language_code === 'en')


  const translations = await getTranslations(parseInt(params.id), selectedLanguage.id)
  const englishTranslations = await getTranslations(parseInt(params.id), english.id)

  const joinedTranslations = joinTranslations(englishTranslations, translations)

  return { props: { project, translations, englishTranslations, joinedTranslations, selectedLanguage } }
}

const ProjectPage: NextPage<StaticProps> = ({ project, selectedLanguage, joinedTranslations }) => {
  return (
    <div>
      <Head>
        <title>Zetkin Translators Interface</title>
        <meta
          name="description"
          content="Editing translations"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <Container>
          <Table>
              <TableHead>
                <TableRow>
                  <TableCell size="small">Dotpath</TableCell>
                  <TableCell>English</TableCell>
                  <TableCell>{selectedLanguage.name}</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {
                  joinedTranslations.map(joinedTranslation => {
                    return (
                      <TableRow key={joinedTranslation.english.id}>
                        <TableCell>
                          {joinedTranslation.english.dotpath}
                        </TableCell>
                        <TableCell>
                          {joinedTranslation.english.text}
                        </TableCell>
                        <TableCell>
                          <TranslationField base={joinedTranslation.english} selected={joinedTranslation.selected}/>
                        </TableCell>
                      </TableRow>
                    )
                  })
                }
              </TableBody>
            </Table> 
        </Container>
      </main>
    </div>
  )
}

export default ProjectPage
