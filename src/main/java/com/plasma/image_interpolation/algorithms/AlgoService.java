package com.plasma.image_interpolation.algorithms;

import java.io.IOException;
import java.nio.file.Paths;

import com.plasma.image_interpolation.Utils.fileUpload;
import com.plasma.image_interpolation.Utils.pythonUtils;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;

import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class AlgoService {

    private final pythonUtils pUtils;

    @Autowired
    public AlgoService(pythonUtils pUtils) {
        this.pUtils = pUtils;
    }

    public void query(MultipartFile multipartFile, String algoType, String scalingVal)
            throws IOException, InterruptedException {

        // First upload the file to the directory
        String fileName = StringUtils.cleanPath(multipartFile.getOriginalFilename());

        log.info(fileName);

        String uploadDir = Paths.get(System.getProperty("user.dir"), "images").toString();

        log.info(uploadDir);

        fileUpload.saveFile(uploadDir, fileName, multipartFile);

        // TODO: QUERY THE PYTHON SERVER TO PROCESS THE FILE AND STORE IT

        pUtils.executeAlgo(algoType, scalingVal, fileName);

        return;
    }

}
