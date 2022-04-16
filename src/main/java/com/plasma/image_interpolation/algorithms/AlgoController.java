package com.plasma.image_interpolation.algorithms;

import java.io.File;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.core.io.Resource;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

@RequestMapping("api/algorithms")
@RestController
@CrossOrigin
public class AlgoController {

    private final AlgoService algoService;

    @Autowired
    public AlgoController(AlgoService algoService) {
        this.algoService = algoService;
    }

    @PostMapping("{algoType}/{scalingValue}")
    public ResponseEntity<String> upSampling(@RequestBody MultipartFile multiPartFile,
            @PathVariable("algoType") String algoType, @PathVariable("scalingValue") String scalingVal)
            throws IOException, InterruptedException {
        algoService.query(multiPartFile, algoType, scalingVal);
        return ResponseEntity.ok("DONE");
    }

    @GetMapping()
    public String getImage() throws IOException {
        return "Hi how are you";
        // File file = new File(Paths.get(System.getProperty("user.dir"), "images",
        // "processedImage.png").toString());
        // if (file.isFile()) {

        // final ByteArrayResource inputStream = new ByteArrayResource(
        // Files.readAllBytes(Paths.get(System.getProperty("user.dir"), "images",
        // "processedImage.png")));
        // return ResponseEntity
        // .ok()
        // .contentType(MediaType.IMAGE_PNG)
        // .body(inputStream);
        // }

        // final ByteArrayResource inputStream = new ByteArrayResource(
        // Files.readAllBytes(Paths.get(System.getProperty("user.dir"), "images",
        // "processedImage.jpg")));
        // return ResponseEntity
        // .ok()
        // .contentType(MediaType.IMAGE_JPEG)
        // .body(inputStream);

    }
}