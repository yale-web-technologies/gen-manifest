import re

class FileNameParser(object):
    def __init__(self, config):
        self.imageServerRootUrl = config['imageServerRootUrl']
        self.manifestServerRootUrl = config['manifestServerRootUrl']
        self.projectPath = config['projectPath']
        self.chapterPrefix = config['chapterPrefix']
        self.pagePrefix = config['pagePrefix']
        self.chapterLabel = config['chapterLabel']
        self.pageLabel = config['pageLabel']

    def parse(self, file_name):
        pattern = r'^(.*%s_(\d\d?)_%s_(\d\d))\.jpf$' % (self.chapterPrefix, self.pagePrefix)
        m = re.match(pattern, file_name)
        if m == None:
            print 'ERROR file name does not match: %s' % file_name
            return None
            
        book_id = m.group(1)
        chapter = m.group(2)
        page = m.group(3)
        
        ident = '%s/%s' % (self.projectPath, book_id)
        
        canvas_id = '%s/canvas/%s' % (self.manifestServerRootUrl, ident)
        canvas_label = '%s %s, %s %s' % (self.chapterLabel, chapter, self.pageLabel, page)
        
        image_id = '%s/annotation/%s' % (self.manifestServerRootUrl, ident)
        image_resource_id = '%s/%s/full/full/0/native.jpg' % (self.imageServerRootUrl, ident)
        image_service_id = '%s/%s' % (self.imageServerRootUrl, ident)
        
        result = dict()
        result['file_name'] = file_name
        result['chapter'] = chapter
        result['page'] = page
        result['canvas_id'] = canvas_id
        result['canvas_label'] = canvas_label
        result['image_id'] = image_id
        result['image_resource_id'] = image_resource_id
        result['image_service_id'] = image_service_id
        return result
