import re

class FileNameParser(object):
    def __init__(self, config):
        self.imageServerRootUrl = config['imageServerRootUrl']
        self.manifestServerRootUrl = config['manifestServerRootUrl']
        self.projectPath = config['projectPath']
        self.chapterNumDigits = config['chapterNumDigits']
        self.pageNumDigits = config['pageNumDigits']
        self.chapterLabel = config['chapterLabel']
        self.pageLabel = config['pageLabel']
        self.imageExtension = config['imageExtension']
        self.createChapters = (config['createChapters'] == 'y')

    def parse(self, file_name):
        if self.createChapters:
            return self.parse_with_chapters(file_name)
        else:
            return self.parse_without_chapters(file_name)

    def parse_without_chapters(self, file_name):
        pattern = r'^%s\.([^.]+)\.%s$' % (self.projectPath,
                                          self.imageExtension)        
        m = re.match(pattern, file_name)
        if m == None:
            print 'ERROR file name does not match: %s' % file_name
            return None

        page_padded = m.group(1)
        
        page_unpadded = re.sub(r'^0+', r'', page_padded)

        ident = '%s-%s-%s' % (self.projectPath, page_padded, self.imageExtension)

        canvas_id = '%s/canvas/%s' % (self.manifestServerRootUrl, ident)
        #canvas_label = '%s %s, %s %s' % (self.chapterLabel, chapter_unpadded, self.pageLabel, page_unpadded)
        canvas_label = 'p. %s' % (page_unpadded)

        image_id = '%s/annotation/%s' % (self.manifestServerRootUrl, ident)
        image_resource_id = '%s/%s/full/full/0/native.jpg' % (self.imageServerRootUrl, ident)
        image_service_id = '%s/%s' % (self.imageServerRootUrl, ident)
        
        result = dict()
        result['file_name'] = file_name
        result['page_padded'] = page_padded
        result['page_unpadded'] = page_unpadded
        result['canvas_id'] = canvas_id
        result['canvas_label'] = canvas_label
        result['image_id'] = image_id
        result['image_resource_id'] = image_resource_id
        result['image_service_id'] = image_service_id
        return result

    def parse_with_chapters(self, file_name):
        pattern = r'^%s\.([^.]+)\.([^.]+)\.%s$' % (self.projectPath,
                                                       self.imageExtension)
        m = re.match(pattern, file_name)
        if m == None:
            print 'ERROR file name does not match: %s' % file_name
            return None

        chapter_padded = m.group(1)
        page_padded = m.group(2)
        
        chapter_unpadded = re.sub(r'^0+', r'', chapter_padded)
        page_unpadded = re.sub(r'^0+', r'', page_padded)

        ident = '%s-%s-%s-%s' % (self.projectPath, chapter_padded, page_padded, self.imageExtension)

        canvas_id = '%s/canvas/%s' % (self.manifestServerRootUrl, ident)
        #canvas_label = '%s %s, %s %s' % (self.chapterLabel, chapter_unpadded, self.pageLabel, page_unpadded)
        canvas_label = '%s.%s' % (chapter_unpadded, page_unpadded)

        image_id = '%s/annotation/%s' % (self.manifestServerRootUrl, ident)
        image_resource_id = '%s/%s/full/full/0/native.jpg' % (self.imageServerRootUrl, ident)
        image_service_id = '%s/%s' % (self.imageServerRootUrl, ident)
        
        result = dict()
        result['file_name'] = file_name
        result['chapter_padded'] = chapter_padded
        result['chapter_unpadded'] = chapter_unpadded
        result['page_padded'] = page_padded
        result['page_unpadded'] = page_unpadded
        result['canvas_id'] = canvas_id
        result['canvas_label'] = canvas_label
        result['image_id'] = image_id
        result['image_resource_id'] = image_resource_id
        result['image_service_id'] = image_service_id
        return result
